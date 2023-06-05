
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from .models import *
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal
from django.views.generic import ListView, View
from django.db.models import F
from django.views import View
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import openpyxl
from openpyxl.styles import Alignment, Font, Border, Side, PatternFill
from openpyxl.styles.colors import WHITE
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image as ExcelImage
from datetime import datetime
from django.template.loader import get_template
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from django.contrib.staticfiles import finders
from PIL import Image as PILImage
from django.urls import reverse
from django.utils.http import urlencode
import time


def index(request):
    unidades = Unidades.objects.all()
    reactivos = Reactivos.objects.all()
    context = {
        'unidades': unidades,
        'reactivos': reactivos
    }
    return render(request, 'reactivos/index.html', context)


def detalle_reactivo(request, pk):

    reactivo = get_object_or_404(Reactivos, pk=pk)
    context = {

        'reactivo': reactivo
    }
    return render(request, 'reactivos/detalle_reactivo.html', context)


def crear_reactivo(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        number = request.POST.get('number')
        number = str(number).zfill(3)
        subnumber = request.POST.get('subnumber')
        if subnumber == '':
            subnumber = '0'

        code = request.POST.get('code')
        name = request.POST.get('name')
        cas = request.POST.get('cas')
        wlocation = request.POST.get('wlocation')

        state = request.POST.get('state')
        state = get_object_or_404(Estados, id=state)

        unit = request.POST.get('unit')
        unit = get_object_or_404(Unidades, id=unit)

        if Reactivos.objects.filter(name=name).exists():
            reactivo = Reactivos.objects.get(name=name)
            reactivo_name = reactivo.name
            messages.error(
                request, 'Ya existe un reactivo con el nombre registrado: '+reactivo_name)
            return HttpResponse('Ya existe un reactivo con el nombre registrado: ' + reactivo_name, status=400)

        if Reactivos.objects.filter(code=code).exists():
            reactivo = Reactivos.objects.get(code=code)
            reactivo_name = reactivo.name
            messages.error(
                request, 'Ya existe un reactivo con el código registrado: '+reactivo_name)
            return HttpResponse('Ya existe un reactivo con el código registrado: ' + reactivo_name, status=400)

        if Reactivos.objects.filter(cas=cas).exists():
            reactivo = Reactivos.objects.get(cas=cas)
            reactivo_name = reactivo.name
            messages.error(
                request, 'Ya existe un reactivo con el CAS registrado: '+reactivo_name)
            return HttpResponse('Ya existe un reactivo con el nombre registrado: ' + reactivo_name, status=400)
            # return redirect('reactivos:crear_reactivo')

        reactivo = Reactivos.objects.create(
            color=color,
            number=number,
            subnumber=subnumber,
            code=code,
            name=name,
            unit=unit,
            cas=cas,
            wlocation=wlocation,
            state=state,
        )

        messages.success(
            request, 'Se ha creado exitosamente el reactivo: '+name)
        return HttpResponse('Reactivo creado correctamente: '+name, status=200)
        # return redirect('reactivos:crear_reactivo')

    context = {
        'unidades': Unidades.objects.all(),
        'estados': Estados.objects.all()
    }
    return render(request, 'reactivos/crear_reactivo.html', context)


def crear_unidades(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre de la unidad
        if Unidades.objects.filter(name=name).exists():
            unidad = Unidades.objects.get(name=name)
            unidad_id = unidad.id
            messages.error(
                request, 'Ya existe una unidad con nombre '+name+' id: '+str(unidad_id))
            return redirect('reactivos:crear_unidades')

        unidad = Unidades.objects.create(
            name=name,
        )
        unidad_id = unidad.id

        messages.success(
            request, 'Se ha creado exitosamente la unidad con nombre '+name+' id: '+str(unidad_id))

        # Agregar el ID de la unidad al contexto para seleccionarla en la plantilla
        context = {'unidad_id': unidad.id, 'unidad_name': unidad.name, }
        return render(request, 'reactivos/crear_unidades.html', context)

    context = {

    }
    return render(request, 'reactivos/crear_unidades.html', context)


# def crear_marca(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         # Verifica si ya existe un registro con el mismo nombre de la marca
#         if Marcas.objects.filter(name=name).exists():
#             messages.error(request, 'Ya existe una marca con nombre: '+name)
#             return redirect('reactivos:crear_marca')

#         marca = Marcas.objects.create(

#             name=name,

#         )
#         messages.success(
#             request, 'Se ha creado exitosamente la marca con nombre: '+name+'.')
#         return redirect('reactivos:crear_marca')

#     context = {

#     }
#     return render(request, 'reactivos/crear_marca.html', context)


def crear_marca(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre de la marca
        if Marcas.objects.filter(name=name).exists():
            marca = Marcas.objects.get(name=name)
            marca_id = marca.id
            messages.error(
                request, 'Ya existe una marca con nombre '+name+' id: '+str(marca_id))
            return redirect('reactivos:crear_marca')

        marca = Marcas.objects.create(

            name=name,

        )
        marca_id = marca.id
        messages.success(
            request, 'Se ha creado exitosamente la marca con nombre '+name+' id: '+str(marca_id))
        return redirect('reactivos:crear_marca')

    context = {

    }
    return render(request, 'reactivos/crear_marca.html', context)


def crear_estado(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre del estado
        if Estados.objects.filter(name=name).exists():
            estado = Estados.objects.get(name=name)
            estado_id = estado.id
            estado_name = estado.name
            messages.error(request, 'Ya existe un estado con nombre ' +
                           estado_name+' id: '+str(estado_id))
            return redirect('reactivos:crear_estado')

        estado = Estados.objects.create(

            name=name,

        )
        estado_id = estado.id
        estado_name = estado.name

        messages.success(
            request, 'Se ha creado exitosamente la presentación con nombre '+estado_name+' id: '+str(estado_id))
        return redirect('reactivos:crear_estado')

    context = {

    }
    return render(request, 'reactivos/crear_estado.html', context)


def crear_facultad(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre del estado
        if Facultades.objects.filter(name=name).exists():
            facultad = Facultades.objects.get(name=name)
            facultad_id = facultad.id
            facultad_name = facultad.name
            messages.error(request, 'Ya existe una facultad con nombre ' +
                           facultad_name+' id: '+str(facultad_id))
            return redirect('reactivos:crear_facultad')

        facultad = Facultades.objects.create(

            name=name,

        )
        facultad_id = facultad.id
        facultad_name = facultad.name

        messages.success(request, 'Se ha creado exitosamente la facultad con nombre ' +
                         facultad_name+' id: '+str(facultad_id))
        return redirect('reactivos:crear_facultad')

    context = {

    }
    return render(request, 'reactivos/crear_facultad.html', context)


def crear_destino(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre del destino
        if Destinos.objects.filter(name=name).exists():
            destino = Destinos.objects.get(name=name)
            destino_id = destino.id
            messages.error(request, 'Ya existe un destino llamado ' +
                           name+' con id: '+str(destino_id))
            return redirect('reactivos:crear_destino')

        destino = Destinos.objects.create(

            name=name,

        )
        destino_id = destino.id
        messages.success(
            request, 'Se ha creado exitosamente el destino con nombre '+name+' con id: '+str(destino_id))
        return redirect('reactivos:crear_destino')

    context = {

    }
    return render(request, 'reactivos/crear_destino.html', context)


def crear_ubicacion(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        facultad = request.POST.get('facultad')
        # Obtiene la instancia de la facultad
        facultad = get_object_or_404(Facultades, id=facultad)

        # Verifica si ya existe un registro con el mismo nombre de la asignatura
        if Ubicaciones.objects.filter(name=name).exists():

            messages.error(
                request, 'Ya existe una ubicación con nombre: '+name)
            return redirect('reactivos:crear_ubicacion')

        asignatura = Ubicaciones.objects.create(

            name=name,
            facultad=facultad,

        )
        messages.success(
            request, 'Se ha creado exitosamente la ubicación con nombre: '+name)
        return redirect('reactivos:crear_ubicacion')
    context = {
        'facultades': Facultades.objects.all()

    }
    return render(request, 'reactivos/crear_ubicacion.html', context)


def crear_responsable(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')

        # Verifica si ya existe un registro con el mismo nombre, telefono o email de la marca
        if Responsables.objects.filter(name=name).exists():
            responsablename = Responsables.objects.get(name=name)
            responsable_name = responsablename.name
            messages.error(
                request, 'Ya existe una responsable con nombre: '+responsable_name)
            return redirect('reactivos:crear_responsable')

        if Responsables.objects.filter(phone=phone).exists():
            responsablename = Responsables.objects.get(phone=phone)
            responsable_name = responsablename.name
            messages.error(
                request, 'Ya existe una responsable con el telefono registrado: '+responsable_name)
            return redirect('reactivos:crear_responsable')

        if Responsables.objects.filter(mail=mail).exists():
            responsablename = Responsables.objects.get(mail=mail)
            responsable_name = responsablename.name
            messages.error(
                request, 'Ya existe una responsable con el email registrado: '+responsable_name)
            return redirect('reactivos:crear_responsable')

        responsable = Responsables.objects.create(

            name=name,
            phone=phone,
            mail=mail,

        )
        messages.success(
            request, 'Se ha creado exitosamente el siguiente responsable: '+name)
        return redirect('reactivos:crear_responsable')

    context = {

    }
    return render(request, 'reactivos/crear_responsable.html', context)


def registrar_salida(request):

    context = {
        'reactivos': Reactivos.objects.all(),
        'responsables': Responsables.objects.all(),
        'marcas': Marcas.objects.all(),
        'ubicaiones': Ubicaciones.objects.all(),
        'destinos': Destinos.objects.all()
    }
    return render(request, 'reactivos/registrar_salida.html', context)


def registrar_salida_confirm(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        nReactivo = name
        try:
            nameReactivo = Reactivos.objects.get(name=name)
            name = nameReactivo
        except Reactivos.DoesNotExist:
            messages.error(request, "El reactivo "+nReactivo +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            name = None
            return redirect('reactivos:registrar_salida_confirm')

        location = request.POST.get('location')
        nlocation = location
        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation
        except Ubicaciones.DoesNotExist:
            messages.error(request, "La ubicación "+nlocation +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            location = None
            return redirect('reactivos:registrar_salida_confirm')

        manager = request.POST.get('manager')
        nmanager = manager
        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request, "El responsable "+nmanager +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            manager = None
            return redirect('reactivos:registrar_salida_confirm')

        trademark = request.POST.get('trademark')
        nMarca = trademark

        try:
            nameMarca = Marcas.objects.get(name=trademark)
            trademark = nameMarca
        except Marcas.DoesNotExist:
            messages.error(request, "La marca "+nMarca +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            trademark = None
            return redirect('reactivos:registrar_salida_confirm')

        destination = request.POST.get('destination')
        nDestino = destination

        try:
            nameDestino = Destinos.objects.get(name=destination)
            destination = nameDestino
        except Marcas.DoesNotExist:
            messages.error(request, "El destino "+nDestino +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            destination = None
            return redirect('reactivos:registrar_salida_confirm')

         # Verificar si el reactivo ya existe en la tabla de inventarios
        try:
            inventario_existente = Inventarios.objects.filter(
                name=name, trademark=trademark).first()

            if inventario_existente:
                weight = request.POST.get('weight')
                weight = Decimal(weight)
                if inventario_existente.weight >= weight:
                    # Si el reactivo ya existe y además hay en el inventario, sumar el peso obtenido del formulario al peso existente
                    weight = request.POST.get('weight')
                    inventario_existente.weight -= int(weight)
                    inventario_existente.save()
                else:
                    messages.error(
                        request, "La cantidad que está tratando de registrar salida supera el stock mínimo en inventario")
                    return redirect('reactivos:registrar_salida_confirm')
            else:
                messages.error(
                    request, "EL reactivo con nombre y marca registradas en el formulario no está en el inventario existente, por favor verifique")
                return redirect('reactivos:registrar_salida_confirm')

        except Inventarios.DoesNotExist:

            weight = request.POST.get('weight')

        if name:

            reference = request.POST.get('reference')
            weight = request.POST.get('weight')
            observations = request.POST.get('observations')
            unit = request.POST.get('unit')

            salida = Salidas.objects.create(
                name=name,
                trademark=trademark,
                reference=reference,
                weight=weight,
                location=location,
                destination=destination,
                manager=manager,
                observations=observations,
            )
            messages.success(request, 'Se ha registrado de manera exitosa la salida del insumo: ' +
                             nReactivo+', cantidad '+weight+' '+unit)
            return redirect('reactivos:registrar_salida_confirm')

    context = {
        'reactivos': Reactivos.objects.all(),
        'destinos': Destinos.objects.all(),
        'responsables': Responsables.objects.all(),
        'marcas': Marcas.objects.all(),
        'ubicaiones': Ubicaciones.objects.all()
    }
    return render(request, 'reactivos/registrar_salida_confirm.html', context)


def registrar_entrada(request):

    context = {
        'reactivos': Reactivos.objects.all(),
        'responsables': Responsables.objects.all(),
        'marcas': Marcas.objects.all(),
        'ubicaiones': Ubicaciones.objects.all()
    }
    return render(request, 'reactivos/registrar_entrada.html', context)


def registrar_entrada_confirm(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        nReactivo = name

        try:
            nameReactivo = Reactivos.objects.get(name=name)
            name = nameReactivo
        except Reactivos.DoesNotExist:
            messages.error(request, "El reactivo "+nReactivo +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            name = None
            return redirect('reactivos:registrar_entrada_confirm')

        location = request.POST.get('location')
        nlocation = location

        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation

        except Ubicaciones.DoesNotExist:
            messages.error(request, "La ubicación "+nlocation +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            location = None
            return redirect('reactivos:registrar_entrada_confirm')

        manager = request.POST.get('manager')
        nmanager = manager

        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request, "El responsable "+nmanager +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            manager = None
            return redirect('reactivos:registrar_entrada_confirm')

        trademark = request.POST.get('trademark')
        nMarca = trademark

        try:
            nameMarca = Marcas.objects.get(name=trademark)
            trademark = nameMarca
        except Marcas.DoesNotExist:
            messages.error(request, "La marca "+nMarca +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            trademark = None
            return redirect('reactivos:registrar_entrada_confirm')

        # Verificar si el reactivo ya existe en la tabla de inventarios
        try:
            inventario_existente = Inventarios.objects.filter(
                name=name, trademark=trademark).first()

            if inventario_existente:
                # Si el reactivo ya existe, sumar el peso obtenido del formulario al peso existente
                weight = request.POST.get('weight')
                inventario_existente.weight += int(weight)
                inventario_existente.save()
            else:
                # Si el reactivo no existe, crear un nuevo registro en la tabla de inventarios
                weight = request.POST.get('weight')

                trademark = request.POST.get('trademark')
                nameMarca = Marcas.objects.get(name=trademark)
                trademark = nameMarca

                name = request.POST.get('name')
                nameReactivo = Reactivos.objects.get(name=name)
                name = nameReactivo

                unit = request.POST.get('unit')
                nameUnidad = Unidades.objects.get(name=unit)
                unit = nameUnidad

                inventario = Inventarios.objects.create(
                    name=name,
                    trademark=trademark,
                    weight=weight,
                    unit=unit,
                )

        except Inventarios.DoesNotExist:
            weight = request.POST.get('weight')

        if name:

            reference = request.POST.get('reference')

            weight = request.POST.get('weight')

            order = request.POST.get('order')

            observations = request.POST.get('observations')
            unit = request.POST.get('unit')

            entrada = Entradas.objects.create(
                name=name,
                trademark=trademark,
                reference=reference,
                weight=weight,
                location=location,
                order=order,
                manager=manager,
                observations=observations,
            )

            messages.success(request, 'Se ha registrado de manera exitosa el ingreso del insumo del insumo: ' +
                             nReactivo+', cantidad '+weight+' '+unit)
            return redirect('reactivos:registrar_entrada_confirm')

    context = {
        'reactivos': Reactivos.objects.all(),
        'responsables': Responsables.objects.all(),
        'marcas': Marcas.objects.all(),
        'ubicaiones': Ubicaciones.objects.all()
    }
    return render(request, 'reactivos/registrar_entrada_confirm.html', context)


class InventarioListView(ListView):
    model = Inventarios
    template_name = "reactivos/inventario.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        # Obtener el número de registros por página de la sesión del usuario
        per_page = request.session.get('per_page')
        if per_page:
            self.paginate_by = int(per_page)
        else:
            self.paginate_by = 10  # Valor predeterminado si no hay variable de sesión

        # Obtener los parámetros de filtrado
        name = request.GET.get('name')
        trademark = request.GET.get('trademark')

        # Guardar los valores de filtrado en la sesión
        request.session['filtered_name'] = name
        request.session['filtered_trademark'] = trademark

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        unique_names_ids = Inventarios.objects.values('name').distinct()
        unique_names = Reactivos.objects.filter(id__in=unique_names_ids)

        unique_trademarks_ids = Inventarios.objects.values(
            'trademark').distinct()
        unique_trademarks = Marcas.objects.filter(id__in=unique_trademarks_ids)

        context['unique_names'] = unique_names
        context['unique_trademarks'] = unique_trademarks

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')
        trademark = self.request.GET.get('trademark')

        if name and trademark:
            queryset = queryset.filter(name=name, trademark=trademark)
        elif name:
            queryset = queryset.filter(name=name)
        elif trademark:
            queryset = queryset.filter(trademark=trademark)

        return queryset


class GuardarPerPageView(View):
    def get(self, request, *args, **kwargs):
        per_page = kwargs.get('per_page')
        request.session['per_page'] = per_page

        # Redirigir a la página de inventario con los parámetros de filtrado actuales
        filtered_name = request.session.get('filtered_name')
        filtered_trademark = request.session.get('filtered_trademark')
        url = reverse('reactivos:inventario')
        params = {}
        if filtered_name:
            params['name'] = filtered_name
        if filtered_trademark:
            params['trademark'] = filtered_trademark
        if params:
            url += '?' + urlencode(params)

        return redirect(url)


class TrademarksAPI(View):
    def get(self, request):
        reactive_id = request.GET.get('reactive_id')

        if reactive_id:
            unique_trademarks = Inventarios.objects.filter(name=reactive_id).values(
                'trademark__id', 'trademark__name').distinct()
        else:
            unique_trademarks = Inventarios.objects.values(
                'trademark__id', 'trademark__name').distinct()

        trademarks_list = list(unique_trademarks)

        return JsonResponse(trademarks_list, safe=False)


def export_to_excel(request):
    # Obtener los valores filtrados almacenados en la sesión del usuario
    name = request.session.get('filtered_name')
    trademark = request.session.get('filtered_trademark')

    # Elimina los valores filtrados de la sesión del usuario
    # del request.session['filtered_name']
    # del request.session['filtered_trademark']

    queryset = Inventarios.objects.all()

    if name and trademark:
        queryset = queryset.filter(name=name, trademark=trademark)
    elif name:
        queryset = queryset.filter(name=name)
    elif trademark:
        queryset = queryset.filter(trademark=trademark)

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Ruta al archivo de imagen del logotipo

    logo_path = finders.find('Images/escudoUnal_black.png')

    # Cargar la imagen y procesarla con pillow
    pil_image = PILImage.open(logo_path)

    # Crear un objeto Image de openpyxl a partir de la imagen procesada
    image = ExcelImage(pil_image)

    # Anclar la imagen a la celda A1
    sheet.add_image(image, 'A1')

    # Obtener la fecha actual
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Unificar las celdas A1, B1, C1 y D1
    sheet.merge_cells('C1:F1')

    sheet['C1'] = 'Inventario de insumos'
    sheet['C2'] = 'Fecha de Creación: '+fecha_creacion
    sheet['A4'] = 'Código'
    sheet['B4'] = 'CAS'
    sheet['C4'] = 'Reactivo'
    sheet['D4'] = 'Marca'
    sheet['E4'] = 'Cantidad'
    sheet['F4'] = 'Unidad'

    # Establecer la altura de la fila 1 y 2 a 30
    sheet.row_dimensions[1].height = 30
    sheet.row_dimensions[2].height = 30

    # Establecer estilo de celda para A1

    cell_A1 = sheet['C1']
    cell_A1.font = Font(bold=True, size=16)

    # Configurar los estilos de borde
    thin_border = Border(left=Side(style='thin'), right=Side(
        style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

    # Establecer el estilo de las celdas A2:D3
    bold_font = Font(bold=True)

    # Establecer el ancho de la columna A a 16
    sheet.column_dimensions['A'].width = 16

    # Establecer el ancho de la columna B a 10
    sheet.column_dimensions['B'].width = 10

    # Establecer el ancho de la columna C a 36
    sheet.column_dimensions['C'].width = 36

    # Establecer el ancho de la columna D a 11
    sheet.column_dimensions['D'].width = 11

    # Establecer el ancho de la columna E a 10
    sheet.column_dimensions['E'].width = 10

    # Establecer el ancho de la columna F a 10
    sheet.column_dimensions['F'].width = 10

    row = 4
    # Aplicar el estilo de borde a las celdas de la fila actual
    for col in range(1, 7):
        sheet.cell(row=row, column=col).border = thin_border
        sheet.cell(row=row, column=col).font = bold_font

    row = 5
    for item in queryset:
        sheet.cell(row=row, column=1).value = item.name.code
        sheet.cell(row=row, column=2).value = item.name.cas
        sheet.cell(row=row, column=3).value = item.name.name
        sheet.cell(row=row, column=4).value = item.trademark.name
        sheet.cell(row=row, column=5).value = item.weight
        sheet.cell(row=row, column=6).value = item.unit.name

        # Aplicar el estilo de borde a las celdas de la fila actual
        for col in range(1, 7):
            sheet.cell(row=row, column=col).border = thin_border

        row += 1

    # Obtén el rango de las columnas de la tabla
    start_column = 1
    end_column = 6
    start_row = 4
    end_row = row - 1

    # Convertir los números de las columnas en letras de columna
    start_column_letter = get_column_letter(start_column)
    end_column_letter = get_column_letter(end_column)

    # Rango de la tabla con el formato "A4:F{n}", donde n es el número de filas en la tabla
    table_range = f"{start_column_letter}{start_row}:{end_column_letter}{end_row}"

    # Agregar filtros solo a las columnas de la tabla
    sheet.auto_filter.ref = table_range

    # Establecer fondo blanco desde la celda A1 hasta el final de la tabla

    fill = PatternFill(fill_type="solid", fgColor=WHITE)
    start_cell = sheet['A1']
    end_column_letter = get_column_letter(end_column+1)
    end_row = row+1
    end_cell = sheet[end_column_letter + str(end_row)]
    table_range = start_cell.coordinate + ':' + end_cell.coordinate

    for row in sheet[table_range]:
        for cell in row:
            cell.fill = fill

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=inventario_insumos.xlsx'

    workbook.save(response)

    return response


def export_to_pdf(request):
    # Obtener los valores filtrados almacenados en la sesión del usuario
    name = request.session.get('filtered_name')
    trademark = request.session.get('filtered_trademark')

    queryset = Inventarios.objects.all()

    if name and trademark:
        queryset = queryset.filter(name=name, trademark=trademark)
    elif name:
        queryset = queryset.filter(name=name)
    elif trademark:
        queryset = queryset.filter(trademark=trademark)
    context = {
        'object_list': queryset
    }

    template = get_template('reactivos/inventario.html')
    context = {
        'object_list': queryset
    }

    html = template.render(context)
    buffer = BytesIO()

    # Crear el archivo PDF
    p = canvas.Canvas(buffer, pagesize=letter)

    # Establecer el tamaño y posición del encabezado
    header_width = 550
    header_height = 40
    header_x = 30
    header_y = 770

    # Cargar la imagen del logotipo
    logo_path = finders.find('Images/escudoUnal_black.png')

    # Cargar la imagen del logotipo y redimensionarla
    # Cargar la imagen del logotipo
    p.drawInlineImage(logo_path, header_x + 10,
                      header_y - 50, width=120, height=70)

    # Dibujar el título del informe con la fecha
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M")
    title_text = f"Inventario de Insumos almacén central de Química\n{fecha_creacion}"
    p.setFont("Helvetica-Bold", 14)

    # Dividir el texto del título en líneas más cortas
    lines = title_text.split('\n')

    # Calcular la altura total del texto del título
    title_height = len(lines) * 5

    # Calcular la posición vertical inicial del título
    title_y = header_y - title_height

    # Dibujar cada línea del texto del título justificada
    for line in lines:
        p.drawRightString(header_x - 50 + header_width, title_y, line)
        title_y -= 20

    # Establecer el tamaño y posición de la tabla

    table_x = header_x
    table_y = header_y - header_height - 30

    # Dibujar la tabla en el PDF
    p.setFont("Helvetica-Bold", 12)  # Configurar la fuente en negrita

    # Ajustar el espaciado inferior de la línea o el espaciado superior del texto para los encabezados
    # Espaciado adicional entre la línea y el texto inferior de los encabezados
    line_space_bottom_header = 6

    # Dibujar línea debajo de los encabezados
    # Establecer el color de la línea (más tenue)
    p.setStrokeColorRGB(0.8, 0.8, 0.8)
    p.setLineWidth(0.5)  # Establecer el grosor de la línea (más delgada)
    p.line(table_x, table_y - line_space_bottom_header, table_x +
           500, table_y - line_space_bottom_header)  # Dibujar línea

    p.drawString(table_x, table_y, "Código")
    p.drawString(table_x + 58, table_y, "CAS")
    p.drawString(table_x + 110, table_y, "Reactivo")
    p.drawString(table_x + 330, table_y, "Marca")
    p.drawString(table_x + 400, table_y, "Cantidad")
    p.drawString(table_x + 460, table_y, "Unidad")

    p.setFont("Helvetica", 12)  # Restaurar la configuración de la fuente

    row_height = 20
    row_y = table_y - row_height

    for item in queryset:
        # Ajustar el espaciado inferior de la línea o el espaciado superior del texto
        line_space_bottom = 12  # Espaciado adicional entre la línea y el texto inferior
        text_space_top = 6  # Espaciado adicional entre el texto superior y la línea

        # Dibujar línea debajo de la fila
        # Establecer el color de la línea (más tenue)
        p.setStrokeColorRGB(0.8, 0.8, 0.8)
        p.setLineWidth(0.5)  # Establecer el grosor de la línea (más delgada)
        p.line(table_x, row_y - line_space_bottom, table_x +
               500, row_y - line_space_bottom)  # Dibujar línea

        # Ajustar la posición del texto
        row_y -= text_space_top

        # Dibujar los contenidos de texto
        p.setFont("Helvetica", 12)
        p.drawString(table_x, row_y, str(item.name.code))
        p.drawString(table_x + 58, row_y, str(item.name.cas))
        p.drawString(table_x + 110, row_y, str(item.name.name))
        p.drawString(table_x + 330, row_y, str(item.trademark.name))
        # Formatear a 1 posición decimal
        p.drawString(table_x + 400, row_y, "{:.1f}".format(item.weight))
        p.drawString(table_x + 460, row_y, str(item.unit.name))
        row_y -= row_height

    p.showPage()
    p.save()

    # Obtener el contenido del archivo PDF generado
    pdf_file = buffer.getvalue()
    buffer.close()

    # Enviar el archivo PDF como respuesta al navegador
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Inventario de Reactivos.pdf"'

    response.write(pdf_file)

    return response


def get_value(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Si la solicitud es una solicitud AJAX, procesar la solicitud y devolver una respuesta JSON
        value_selected = request.GET.get('value_selected')
        try:
            # Intentar obtener el valor correspondiente de la base de datos
            reactivo = Reactivos.objects.get(name=value_selected)
            cas = reactivo.cas
            codigo = reactivo.code
            liquid = reactivo.state.name
            nombre_unit = reactivo.unit.name  # Obtener el nombre de la unidad
        except Reactivos.DoesNotExist:
            # Si el reactivo no existe, devolver un valor por defecto
            cas = ""
            codigo = ""
            liquid = ''
            nombre_unit = ""

        return JsonResponse({
            'cas': cas,
            'codigo': codigo,
            'liquid': liquid,
            'nombre_unit': nombre_unit  # Pasar el nombre de la unidad
        })
    else:
        # Si la solicitud no es una solicitud AJAX, devolver una respuesta HTTP 400 Bad Request
        return HttpResponseBadRequest()


def autocomplete(request):
    term = request.GET.get('term', '')
    reactivos = Reactivos.objects.filter(Q(name__icontains=term) | Q(
        code__icontains=term) | Q(cas__icontains=term))[:10]
    results = []
    for reactivo in reactivos:
        result = {
            'id': reactivo.id,
            'name': reactivo.name,
            'code': reactivo.code,
            'cas': reactivo.cas
        }
        results.append(result)

    return JsonResponse(results, safe=False)


def autocomplete_out(request):
    term = request.GET.get('term', '')
    inventarios = Inventarios.objects.filter(
        Q(name__name__icontains=term) | Q(name__code__icontains=term) | Q(name__cas__icontains=term))[:10]
    results = []
    for inventario in inventarios:
        result = {
            'id': inventario.name.id,
            'name': inventario.name.name,
            'code': inventario.name.code,
            'cas': inventario.name.cas,
        }
        results.append(result)

    return JsonResponse(results, safe=False)


def autocomplete_location(request):
    term = request.GET.get('term', '')
    ubicaciones = Ubicaciones.objects.filter(Q(name__icontains=term))[:10]
    results = []
    for ubicacion in ubicaciones:
        results.append({'value': ubicacion.name})
    pass

    return JsonResponse(results, safe=False)


def autocomplete_manager(request):
    term = request.GET.get('term', '')
    responsables = Responsables.objects.filter(Q(name__icontains=term))[:10]
    results = []
    for responsable in responsables:
        results.append({'value': responsable.name})
    pass

    return JsonResponse(results, safe=False)
