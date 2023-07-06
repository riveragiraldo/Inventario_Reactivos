#Diferentes vistas y/o APIS que interactuan el front con back

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
from django.core.exceptions import ObjectDoesNotExist

# Vista para la creación del index, aun no se define contexto dependiendo de los enlaces a mostrar
def index(request):
    unidades = Unidades.objects.all()
    reactivos = Reactivos.objects.all()
    context = {
        
    }
    return render(request, 'reactivos/index.html', context)

# Vista para la creación del detalle del reactivo, hasta el momento solo tiene contexto el reactivo, pero se le puede poner lo necesario
def detalle_reactivo(request, pk):

    reactivo = get_object_or_404(Reactivos, pk=pk)
    context = {

        'reactivo': reactivo
    }
    return render(request, 'reactivos/detalle_reactivo.html', context)

# La vista "crear_reactivo" se encarga de gestionar la creación de un reactivo. Esta vista toma los datos del formulario 
# existente en el template "crear_reactivo.html" y realiza las operaciones necesarias en la base de datos para almacenar 
# la información del reactivo. Esto puede incluir la validación de los datos ingresados, la creación de un nuevo registro 
# en la tabla correspondiente y cualquier otra gestión requerida para asegurar la integridad de los datos en la base de datos.
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
        
        state = request.POST.get('state')
        state = get_object_or_404(Estados, id=state)

        unit = request.POST.get('unit')
        unit = get_object_or_404(Unidades, id=unit)

        sga = request.POST.get('sga')
        sga = get_object_or_404(SGA, id=sga)

        respel = request.POST.get('respel')
        respel = get_object_or_404(RespelC, id=respel)

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
            
        reactivo = Reactivos.objects.create(
            color=color,
            number=number,
            subnumber=subnumber,
            code=code,
            name=name,
            unit=unit,
            cas=cas,
            state=state,
            sga=sga,
            respel=respel,
        )
        
        messages.success(request, 'Se ha creado exitosamente el reactivo: '+name)
        return HttpResponse('Reactivo creado correctamente: '+name, status=200)
    
    context = {
        'unidades': Unidades.objects.all(),
        'estados': Estados.objects.all(),
        'respels': RespelC.objects.all(),
        'sgas': SGA.objects.all(),
    }
    
    return render(request, 'reactivos/crear_reactivo.html', context)

# La vista "crear_unidades" se encarga de gestionar la creación de unidades. Esta vista toma los datos del formulario 
# existente en el template "crear_unidades.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Unidades". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la unidad
# ya existe en la base de datos antes de crearla. Si la unidad es única, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Unidades". Si la unidad ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.

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

# La vista "crear_respel" se encarga de gestionar la creación de clasificación respel. Esta vista toma los datos del formulario 
# existente en el template "crear_respel.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "RespelC". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la clasifciación respel
# ya existe en la base de datos antes de crearla. Si la clasificación es única, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "RespelC". Si la clasificación ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
def crear_respel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Verifica si ya existe un registro con el mismo nombre de la marca
        if RespelC.objects.filter(name=name).exists():
            respel = RespelC.objects.get(name=name)
            respel_id = respel.id
            messages.error(
                request, 'Ya existe una clasificación Respel con nombre '+name+' id: '+str(respel_id))
            return redirect('reactivos:crear_respel')

        respel = RespelC.objects.create(

            name=name,
            description=description,

        )
        respel_id = respel.id
        messages.success(
            request, 'Se ha creado exitosamente la clasificación Respel con nombre '+name+' id: '+str(respel_id))
        return redirect('reactivos:crear_respel')

    context = {

    }
    return render(request, 'reactivos/crear_respel.html', context)


# La vista "crear_sga" se encarga de gestionar la creación de codificación SGA. Esta vista toma los datos del formulario 
# existente en el template "crear_sga.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "SGA". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la codificación SGA
# ya existe en la base de datos antes de crearla. Si la codificación es única, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "SGA". Si la codificación ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
def crear_sga(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Verifica si ya existe un registro con el mismo nombre de la marca
        if SGA.objects.filter(name=name).exists():
            sga = SGA.objects.get(name=name)
            sga_id = sga.id
            messages.error(
                request, 'Ya existe una codificación SGA con nombre '+name+' id: '+str(sga_id))
            return redirect('reactivos:crear_sga')

        sga = SGA.objects.create(

            name=name,
            description=description,

        )
        sga_id = sga.id
        messages.success(
            request, 'Se ha creado exitosamente la codificación SGA con nombre '+name+' id: '+str(sga_id))
        return redirect('reactivos:crear_sga')

    context = {

    }
    return render(request, 'reactivos/crear_sga.html', context)

# La vista "crear_marca" se encarga de gestionar la creación de marcas en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_marca.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Marcas". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la marca
# ya existe en la base de datos antes de crearla. Si la marca es única, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Marcas". Si la marca ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
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

# La vista "crear_walmacen" es responsable de la creación de ubicaciones en el almacén dentro de la base de datos. Los 
# datos se obtienen del formulario presente en el template "crear_walmacen.html", y se realizan las operaciones necesarias 
# en la base de datos utilizando el modelo "Almacenamiento". El objetivo es asegurar la unicidad de los registros, lo cual 
# implica verificar si la ubicación en el almacén ya existe antes de crearla, considerando la clave foránea "lab". Si la 
# ubicación es única para un laboratorio específico, se crea un nuevo registro en la tabla correspondiente utilizando el 
# modelo "Almacenamiento". En caso de que la ubicación ya exista dentro del laboratorio, se muestra un mensaje de error o 
# se toma la acción apropiada según los requisitos del sistema.
def crear_walmacen(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        lab = request.POST.get('lab')
        nlab = lab

        try:
            namelab = Laboratorios.objects.get(name=lab)
            lab = namelab
        except Laboratorios.DoesNotExist:
            messages.error(request, "El Laboratorio "+nlab +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            lab = None
            return HttpResponse("El laboratorio "+nlab +
                           " no se encuentra en la base de datos, favor crearlo primero.", status=400)

       # Verifica si ya existe un registro con el mismo nombre y laboratorio
        if Almacenamiento.objects.filter(name=name, lab=lab).exists():
            w_location = Almacenamiento.objects.get(name=name, lab=lab)
            wlocation_id = w_location.id
            messages.error(request, "Ya existe una ubicación en almacén con nombre "+name+' id: '+str(wlocation_id))
            return redirect('reactivos:crear_walmacen')
        
        wubicaciones = Almacenamiento.objects.create(
            name=name,
            description=description,
            lab=lab,
        )

        wubicacion_id = wubicaciones.id
        messages.success(
            request, 'Se ha creado exitosamente la ubicacion en almacén con nombre '+name+' id: '+str(wubicacion_id))
        return redirect('reactivos:crear_walmacen')

    context = {
        'laboratorios': Laboratorios.objects.all()
    }
    return render(request, 'reactivos/crear_walmacen.html', context)


# La vista "crear_estado" se encarga de gestionar la creación de estados en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_estado.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Estados". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si el estado
# ya existe en la base de datos antes de crearlo. Si el estado es única, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Estados". Si el estado ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.

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

# La vista "crear_laboratorio" se encarga de gestionar la creación de estados en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_laboratorio.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Laboratorios". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si el laboratorio
# ya existe en la base de datos antes de crearlo. Si el laboratorio es único, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Laboratorios". Si el estado ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
def crear_laboratorio(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre del laboratorio
        if Laboratorios.objects.filter(name=name).exists():
            laboratorio = Laboratorios.objects.get(name=name)
            laboratorio_id = laboratorio.id
            laboratorio_name = laboratorio.name
            messages.error(request, 'Ya existe un laboratorio con nombre ' +
                           laboratorio_name+' id: '+str(laboratorio_id))
            return redirect('reactivos:crear_laboratorio')

        laboratorio = Laboratorios.objects.create(

            name=name,

        )
        laboratorio_id = laboratorio.id
        laboratorio_name = laboratorio.name

        messages.success(request, 'Se ha creado exitosamente el laboratorio con nombre ' +
                         laboratorio_name+' id: '+str(laboratorio_id))
        return redirect('reactivos:crear_laboratorio')

    context = {

    }
    return render(request, 'reactivos/crear_laboratorio.html', context)


# La vista "crear_facultad" se encarga de gestionar la creación de estados en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_facultad.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Facultades". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la facultad
# ya existe en la base de datos antes de crearlo. Si la facultad es único, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Facultades". Si la facultad ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
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

# La vista "crear_destino" se encarga de gestionar la creación de destinos en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_destino.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Destinos". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si el destino
# ya existe en la base de datos antes de crearlo. Si este es único, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Destinos". Si el destino ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
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

# La vista "crear_destino" se encarga de gestionar la creación de ubicaciones en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_ubicaciones.html" y realiza las operaciones necesarias en la base de datos utilizando 
# el modelo "Ubicaciones". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la ubicación
# ya existe en la base de datos antes de crearlo. Si este es único, se crea un nuevo registro en la tabla 
# correspondiente utilizando el modelo "Ubicaciones". Si la ubicación ya existe, se muestra un mensaje de error o se toma la 
# acción apropiada según los requisitos del sistema.
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

#La vista "crear_responsable" se encarga de gestionar la creación de responsables en la db. Esta vista toma los datos del formulario 
# existente en el template "crear_responsables.html" y realiza las operaciones necesarias en la base de datos utilizando el modelo 
# "Responsables". El objetivo es garantizar la unicidad de los registros, lo que implica verificar si la el responsable ya existe en la 
# base de datos antes de crearlo, para ello, realiza verificación por nombre, correo electrónico y teléfono. Si este es único, se crea 
# un nuevo registro en la tabla correspondiente utilizando el modelo "Responsables". Si el responsable ya existe, se muestra un mensaje 
# de error o se toma la acción apropiada según los requisitos del sistema.
def crear_responsable(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        prefix = request.POST.get('prefix')

        # Añadir la secuencia de escape "\+" al prefijo
        if prefix.startswith("+"):
            prefix = "\\" + prefix
        # Eliminar los caracteres de escape
        prefix = prefix.strip("\\")

        phone = prefix + phone
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

# La vista "registrar_entrada" se encarga de gestionar el registro de transacciones de entrada en el aplicativo de insumos en la base de 
# datos. Los datos se obtienen del formulario presente en el template "registrar_entrada.html". Utilizando el modelo "Entradas", se 
# realizan las operaciones necesarias. La vista verifica la existencia de los campos de entrada que son foráneos en la base de datos. 
# Si alguno de estos campos es tomado como un nombre o un ID, se convierten en una instancia del modelo foráneo correspondiente. 
# Luego, se verifica en la tabla "Inventarios" si existe algún registro que coincida con los campos "lab", "name", "trademark" y 
# "reference". Si hay una coincidencia, se suma el valor del campo "weight" del registro existente. En caso contrario, se crea un nuevo 
# registro con los valores correspondientes.Finalmente, se realiza la creación del registro de entrada en la base de datos utilizando 
# el modelo "Entradas".
def registrar_entrada(request):

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
            return HttpResponse("El reactivo "+nReactivo +" no se encuentra en la base de datos, favor crearlo primero.", status=400)

        location = request.POST.get('location')
        nlocation = location
        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation

        except Ubicaciones.DoesNotExist:
            messages.error(request, "La ubicación "+nlocation +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            location = None
            return HttpResponse("La ubicación "+nlocation +" no se encuentra en la base de datos, favor crearlo primero.", status=400)
        
        manager = request.POST.get('manager')
        nmanager = manager
        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request, "El responsable "+nmanager +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            manager = None
            return HttpResponse("El responsable "+nmanager +
                           " no se encuentra en la base de datos, favor crearlo primero.", status=400)
                
        trademark_id = request.POST.get('trademark')
        try:
            nameMarca = Marcas.objects.get(id=trademark_id)
            trademark = nameMarca
        except ObjectDoesNotExist:
            trademark = None
            return redirect('reactivos:registrar_entrada')
        
        
        wlocation_id = request.POST.get('wlocation')
        try:
            nameWlocation = Almacenamiento.objects.get(id=wlocation_id)
            wlocation = nameWlocation
        except ObjectDoesNotExist:
            wlocation = None
            return redirect('reactivos:registrar_entrada')        
        
        destination_id = request.POST.get('destination')
        try:
            namedestino = Destinos.objects.get(id=destination_id)
            destination = namedestino
        except ObjectDoesNotExist:
            destination = None
            return redirect('reactivos:registrar_entrada')
        
        lab = request.POST.get('lab')
        nlab = lab
        try:
            namelab = Laboratorios.objects.get(name=lab)
            lab = namelab
        except Laboratorios.DoesNotExist:
            messages.error(request, "El Laboratorio "+nlab +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            lab = None
            return HttpResponse("El Laboratorio "+nlab +
                           " no se encuentra en la base de datos, favor crearlo primero.", status=400)
        
        reference = request.POST.get('reference')
        
        
        # Verificar si el reactivo ya existe en la tabla de inventarios
        try:
            inventario_existente = Inventarios.objects.filter(
                name=name, trademark=trademark, reference=reference, lab=lab).first()

            if inventario_existente:
                # Si el reactivo ya existe y está activo(cantidad>0), sumar el peso obtenido del formulario al peso existente
                if inventario_existente.is_active == True:
                    # Si el reactivo ya existe, sumar el peso obtenido del formulario al peso existente
                    weight = request.POST.get('weight')
                    inventario_existente.weight += int(weight)
                    inventario_existente.edate = request.POST.get('edate')
                    inventario_existente.wlocation = wlocation
                    minstock = request.POST.get('minstock')
                    if minstock=='':
                        minstock=0
                    inventario_existente.minstock = minstock
                    inventario_existente.save()
                # Si el reactivo ya existe y NO está activo(cantidad00), poner is_active=True y sumar el peso obtenido del formulario al peso existente    
                else:
                    inventario_existente.is_active= True
                    weight = request.POST.get('weight')
                    inventario_existente.weight += int(weight)
                    inventario_existente.edate = request.POST.get('edate')
                    inventario_existente.wlocation = wlocation
                    minstock = request.POST.get('minstock')
                    if minstock=='':
                        minstock=0
                    inventario_existente.minstock = minstock
                    inventario_existente.save()
            else:
                # Si el reactivo no existe, crear un nuevo registro en la tabla de inventarios
                weight = request.POST.get('weight')

                trademark_id = request.POST.get('trademark')
                try:
                    nameMarca = Marcas.objects.get(id=trademark_id)
                    trademark = nameMarca
                except ObjectDoesNotExist:
                    trademark = None
                    return redirect('reactivos:registrar_entrada')

                name = request.POST.get('name')
                nameReactivo = Reactivos.objects.get(name=name)
                name = nameReactivo
                reference = request.POST.get('reference')
                edate = request.POST.get('edate')
                minstock = request.POST.get('minstock')
                if minstock=='':
                    minstock=0

                unit_id = request.POST.get('unit')
                try:
                    nameUnidad = Unidades.objects.get(name=unit_id)
                    unit = nameUnidad
                except ObjectDoesNotExist:
                    unit = None
                    return redirect('reactivos:registrar_entrada')
                

                inventario = Inventarios.objects.create(
                    name=name,
                    trademark=trademark,
                    weight=weight,
                    unit=unit,
                    reference=reference,
                    lab=lab,
                    wlocation=wlocation,
                    minstock=minstock,
                    edate=edate,
                
                )

        except Inventarios.DoesNotExist:
            weight = request.POST.get('weight')
                       
        if name:

            
            weight = request.POST.get('weight')
            order = request.POST.get('order')
            observations = request.POST.get('observations')
            unit = request.POST.get('unit')
            nproject = request.POST.get('nproject')
            price = request.POST.get('price')
            

            entrada = Entradas.objects.create(
                name=name,
                trademark=trademark,
                reference=reference,
                weight=weight,
                location=location,
                order=order,
                manager=manager,
                observations=observations,
                nproject=nproject,
                price=price,
                destination=destination,
                lab=lab,
            )

            messages.success(request, 'Se ha registrado de manera exitosa el ingreso del insumo: ' +
                             nReactivo+', cantidad '+weight+' '+unit)
            return HttpResponse('Se ha registrado de manera exitosa el ingreso del: ' +
                             nReactivo+', cantidad '+weight+' '+unit, status=200)
    context = {
                'reactivos': Reactivos.objects.all(),
                'responsables': Responsables.objects.all(),
                'marcas': Marcas.objects.all(),
                'ubicaiones': Ubicaciones.objects.all(),
                'destinos':Destinos.objects.all(),
                'laboratorios':Laboratorios.objects.all(),
                'wubicaciones':Almacenamiento.objects.all(),
            }
        
    return render(request, 'reactivos/registrar_entrada.html', context)


# La vista "registrar_salida" se encarga de gestionar el registro de transacciones de salida en el aplicativo de insumos de la base de 
# datos. Los datos se obtienen del formulario presente en el template "registrar_salida.html" y se utilizan el modelo "Salidas" para 
# realizar las operaciones correspondientes de inserción de registros.
# En esta vista se verifica la existencia de los campos de entrada que son foráneos en la base de datos. En caso de que alguno de estos 
# campos sea tomado como un nombre o un ID, se convierten en una instancia del modelo foráneo correspondiente. Luego, se realiza una 
# verificación en la tabla "Inventarios" para comprobar si existe algún registro que coincida con los campos "lab", "name", "trademark" 
# y "reference".
#Si se encuentra una coincidencia en "Inventarios", se resta el valor del campo "weight" del registro existente. Si no hay una 
# coincidencia, se impide el registro tanto en la tabla "Inventarios" como en la tabla "Salidas". Además, se verifica que el campo 
# "weight" sea mayor o igual para permitir la transacción. En caso contrario, se muestra un mensaje de error. Adicionalmente, si el 
# campo "weight" llega a cero después de realizar el registro, se muestra un mensaje indicando que el insumo ha alcanzado el valor de cero.
#Finalmente, se realiza la creación del registro de salida en la base de datos utilizando el modelo "Salidas".
def registrar_salida(request):

    if request.method == 'POST': 
        warning=""
        
        name = request.POST.get('name')
        nReactivo = name
        try:
            nameReactivo = Reactivos.objects.get(name=name)
            name = nameReactivo
        except Reactivos.DoesNotExist:
            messages.error(request, "El reactivo "+nReactivo +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            name = None
            return HttpResponse("El reactivo "+nReactivo +" no se encuentra en la base de datos, favor crearlo primero.", status=400)

        location = request.POST.get('location')
        nlocation = location
        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation
        except Ubicaciones.DoesNotExist:
            messages.error(request, "La ubicación "+nlocation +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            location = None
            return HttpResponse("La ubicación "+nlocation +" no se encuentra en la base de datos, favor crearlo primero.", status=400)
        
        manager = request.POST.get('manager')
        nmanager = manager
        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request, "El responsable "+nmanager +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            manager = None
            return HttpResponse("El responsable "+nmanager +
                           " no se encuentra en la base de datos, favor crearlo primero.", status=400)
        
        trademark_id = request.POST.get('trademark')
        try:
            nameMarca = Marcas.objects.get(id=trademark_id)
            trademark = nameMarca
        except ObjectDoesNotExist:
            trademark = None
            return redirect('reactivos:registrar_salida')

        destination_id = request.POST.get('destination')
        try:
            namedestino = Destinos.objects.get(id=destination_id)
            destination = namedestino
        except ObjectDoesNotExist:
            destination = None
            return redirect('reactivos:registrar_salida')
        
        lab = request.POST.get('lab')
        nlab = lab
        try:
            namelab = Laboratorios.objects.get(name=lab)
            lab = namelab
        except Laboratorios.DoesNotExist:
            messages.error(request, "El Laboratorio "+nlab +
                           " no se encuentra en la base de datos, favor crearlo primero.")
            lab = None
            return HttpResponse("El responsable "+nlab +
                           " no se encuentra en la base de datos, favor crearlo primero.", status=400)
        
        reference = request.POST.get('reference')
        
        # Verificar si el reactivo ya existe en la tabla de inventarios
        try:
            inventario_existente = Inventarios.objects.filter(
                name=name, trademark=trademark, reference=reference, lab=lab).first()

            if inventario_existente:
                
                weight = request.POST.get('weight')
                weight=Decimal(weight)
                unit = request.POST.get('unit')
                #Verificar si la cantidad actual sea mayor o igual a cantidad registrada
                if inventario_existente.weight>=weight:
                    inventario_existente.weight -= int(weight)
                    inventario_existente.save()
                    #Verificación después de restar en la tabla llegue a cero y ponga en warning la alerta que 
                    # posteriormente se enviará al usuario informando
                    if inventario_existente.weight == 0:
                        inventario_existente.is_active = False  # Asignar False a la columna is_active
                        inventario_existente.save()
                        warning=", pero el inventario actual ha llegado a 0. Favor informar al coordinador de laboratorio."
                else:
                    inventario_existente.weight=int(inventario_existente.weight)
                    messages.error(request, "No es posible realizar la salida del reactivo "+inventario_existente.name.name+": Inventario actual: " + str(inventario_existente.weight) + ", " + unit + " Cantidad solicitada: " + str(weight) + " " + unit)
                    return HttpResponse("Error de cantidades al insertar en la base de datos", status=400)
            else:
                
                messages.error(request, "Los valor seleccionados (Reactivo, Marca o referencia) no corresponden a un insumo existente en el inventario, verifique de nuevo")
                return HttpResponse("Error al insertar en la base de datos", status=400)

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
                manager=manager,
                observations=observations,
                destination=destination,
                lab=lab,
            )

            messages.success(request, 'Se ha registrado de manera exitosa la salida del insumo del insumo: ' +
                             nReactivo+', cantidad '+weight+' '+unit+warning)
            return HttpResponse('Se ha registrado de manera exitosa la salida del insumo : ' +
                             nReactivo+', cantidad '+weight+' '+unit+warning, status=200)
    context = {
                'reactivos': Reactivos.objects.all(),
                'responsables': Responsables.objects.all(),
                'marcas': Marcas.objects.all(),
                'ubicaiones': Ubicaciones.objects.all(),
                'destinos':Destinos.objects.all(),
                'referencias':Inventarios.objects.all(),
                'laboratorios':Laboratorios.objects.all(),
            }
        
    return render(request, 'reactivos/registrar_salida.html', context)

# La vista "inventario" se encarga de obtener los valores de la tabla del modelo "Inventario" y los envía al template "inventario.html"
# Además, recibe los valores filtrados desde el template, especificando qué elementos se desean mostrar en la lista. Estos valores 
# filtrados, como el nombre y la marca, se guardan en la sesión utilizando los siguientes comandos:
# request.session['filtered_name'] = name
# request.session['filtered_trademark'] = trademark
# Esto permite que los valores de filtrado puedan ser utilizados en otras vistas que realicen la exportación a formatos como Excel o 
# PDF. De esta manera, se garantiza la consistencia de los datos filtrados al exportarlos a otros formatos.

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
        lab = request.GET.get('lab')
        name = request.GET.get('name')
        trademark = request.GET.get('trademark')
        reference = request.GET.get('reference')

        # Guardar los valores de filtrado en la sesión
        request.session['filtered_lab'] = lab
        request.session['filtered_name'] = name
        request.session['filtered_trademark'] = trademark
        request.session['filtered_reference'] = reference

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        unique_labs_ids = Inventarios.objects.values('lab').distinct()
        unique_labs = Laboratorios.objects.filter(id__in=unique_labs_ids)

        unique_names_ids = Inventarios.objects.values('name').distinct()
        unique_names = Reactivos.objects.filter(id__in=unique_names_ids)

        unique_trademarks_ids = Inventarios.objects.values(
            'trademark').distinct()
        unique_trademarks = Marcas.objects.filter(id__in=unique_trademarks_ids)
        
        unique_references = Inventarios.objects.values(
            'reference').distinct()

        context['unique_labs'] = unique_labs
        context['unique_names'] = unique_names
        context['unique_trademarks'] = unique_trademarks
        context['unique_references'] = unique_references

        # Obtener la lista de inventarios
        inventarios = context['object_list']

        # Recorrer los inventarios y cambiar el formato de la fecha
        for inventario in inventarios:
            # Obtener la fecha de vencimiento
            edate = inventario.edate

            # Cambiar el formato de fecha de inglés a formato dd/mm/aaaa
            edate = edate.strftime('%d/%m/%Y')

            # Actualizar la fecha en el inventario
            inventario.edate = edate

        context['object_list'] = inventarios

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort')
        queryset = queryset.order_by('id')

        lab = self.request.GET.get('lab')
        name = self.request.GET.get('name')
        trademark = self.request.GET.get('trademark')
        reference = self.request.GET.get('reference')

        if lab and name and trademark and reference:
            queryset = queryset.filter(lab=lab, name=name, trademark=trademark, reference=reference, is_active=True)
        elif lab and name and trademark:
            queryset = queryset.filter(lab=lab, name=name, trademark=trademark, is_active=True)
        elif lab and name and reference:
            queryset = queryset.filter(lab=lab, name=name, reference=reference, is_active=True)
        elif lab and reference and trademark:
            queryset = queryset.filter(lab=lab, reference=reference, trademark=trademark, is_active=True)
        elif name and reference and trademark:
            queryset = queryset.filter(name=name, reference=reference, trademark=trademark, is_active=True)
        elif lab and name:
            queryset = queryset.filter(lab=lab, name=name, is_active=True)
        elif lab and trademark:
            queryset = queryset.filter(lab=lab, trademark=trademark, is_active=True)
        elif lab and reference:
            queryset = queryset.filter(lab=lab, reference=reference, is_active=True)
        elif name and reference:
            queryset = queryset.filter(name=name, reference=reference, is_active=True)
        elif name and trademark:
            queryset = queryset.filter(name=name, trademark=trademark, is_active=True)
        elif reference and trademark:
            queryset = queryset.filter(reference=reference, trademark=trademark, is_active=True)
        elif lab:
            queryset = queryset.filter(lab=lab, is_active=True)
        elif name:
            queryset = queryset.filter(name=name, is_active=True)
        elif trademark:
            queryset = queryset.filter(trademark=trademark, is_active=True)
        elif reference:
            queryset = queryset.filter(reference=reference, is_active=True)
        else:
            queryset = queryset.filter(is_active=True)

        if sort_by:
            if sort_by == 'code':
                queryset = queryset.order_by('name__code')
            elif sort_by == 'cas':
                queryset = queryset.order_by('name__cas')
            elif sort_by == 'name':
                queryset = queryset.order_by('name__name')
            elif sort_by == 'trademark':
                queryset = queryset.order_by('trademark__name')
            elif sort_by == 'reference':
                queryset = queryset.order_by('reference')
            elif sort_by == 'weight':
                queryset = queryset.order_by('weight')
            elif sort_by == 'unit':
                queryset = queryset.order_by('unit__name')
            elif sort_by == 'wlocation':
                queryset = queryset.order_by('wlocation__name')
            elif sort_by == 'lab':
                queryset = queryset.order_by('lab__name')
            elif sort_by == 'edate':
                queryset = queryset.order_by('edate')

        return queryset

# Guarda los datos de filtrados y datos de paginación en el template inventarios.html en los datos de session de usuario
class GuardarPerPageView(View):
    def get(self, request, *args, **kwargs):
        per_page = kwargs.get('per_page')
        request.session['per_page'] = per_page

        # Redirigir a la página de inventario con los parámetros de filtrado actuales
        filtered_lab = request.session.get('filtered_lab')
        filtered_name = request.session.get('filtered_name')
        filtered_trademark = request.session.get('filtered_trademark')
        filtered_reference = request.session.get('filtered_reference')
        
        url = reverse('reactivos:inventario')
        params = {}
        if filtered_lab:
            params['lab'] = filtered_lab
        if filtered_name:
            params['name'] = filtered_name
        if filtered_trademark:
            params['trademark'] = filtered_trademark
        if filtered_reference:
            params['reference'] = filtered_reference
        
        if params:
            url += '?' + urlencode(params)

        return redirect(url)

# Devuelve valores de name, trademark y reference para ser insertados los select correspondientes en el template Inventarios al modificar 
# el select name

class NamesTrademarksAndReferencesByLabAPI(View):
    def get(self, request):
        lab = request.GET.get('lab')

        inventarios = Inventarios.objects.all()

        if lab:
            inventarios = inventarios.filter(lab=lab)

        names = inventarios.values('name', 'name__name').distinct().order_by('name__name')
        trademarks = inventarios.values('trademark', 'trademark__name').distinct().order_by('trademark__name')
        references = inventarios.values('reference').distinct().order_by('reference')

        names_trademarks_and_references_list = {
            'names': list(names),
            'trademarks': list(trademarks),
            'references': list(references)
        }

        return JsonResponse(names_trademarks_and_references_list, safe=False)


    
# Devuelve valores de trademark y reference para ser insertados los select correspondientes en el template Inventarios al modificar 
# name de reactivo
class TrademarksAndReferencesByNameAPI(View):
    def get(self, request):
        name = request.GET.get('name')
        lab = request.GET.get('lab')

        inventarios = Inventarios.objects.all()

        if name:
            inventarios = inventarios.filter(name=name, lab=lab)

        trademarks_and_references = inventarios.values('trademark', 'trademark__name', 'reference').distinct()
        trademarks_and_references_list = list(trademarks_and_references)

        return JsonResponse(trademarks_and_references_list, safe=False)
    
# Devuelve valores de reference para ser insertados los select correspondientes en el template Inventarios al modificar 
# trademark de reactivo
class ReferencesByTrademarkAPI(View):
    def get(self, request):
        lab = request.GET.get('lab')
        name = request.GET.get('name')
        trademark = request.GET.get('trademark')

        inventarios = Inventarios.objects.all()

        if name:
            inventarios = inventarios.filter(name=name, lab=lab, trademark=trademark)

        references = inventarios.values('reference').distinct()
        references_list = list(references)

        return JsonResponse(references_list, safe=False)



    
# Devuelve al template los valores únicos de wlocation según el nombre del reactivo en la tabla del modelo Almacenamiento
class WlocationsAPI(View):
    def get(self, request):
        lab = request.GET.get('lab')
        
        if lab:
            almacenamiento = Almacenamiento.objects.filter(lab__name=lab)
            wlocation_list = almacenamiento.values('id','name').distinct()
            return JsonResponse(list(wlocation_list), safe=False)

        return JsonResponse([], safe=False)

# Utilizando los valores filtrados en el template inventario.html, y guardados en los datos de sesión, se crea el archivo de Excel 
# correspondiente e se introducen los valores desde la tabla del modelo Inventarios. Además, se aplican formatos a los encabezados, se 
# coloca un título, la fecha de creación y el logo. También se ajustan los anchos de columna y las alturas de fila, y se añaden filtros 
# a los encabezados en caso de que el usuario lo solicite

def export_to_excel(request):
    # Obtener los valores filtrados almacenados en la sesión del usuario
    lab = request.session.get('filtered_lab')
    name = request.session.get('filtered_name')
    trademark = request.session.get('filtered_trademark')
    reference = request.session.get('filtered_reference')


    queryset = Inventarios.objects.all()

    if lab and name and trademark and reference:
            queryset = queryset.filter(lab=lab, name=name, trademark=trademark, reference=reference, is_active=True)
    elif lab and name and trademark:
        queryset = queryset.filter(lab=lab, name=name, trademark=trademark, is_active=True)
    elif lab and name and reference:
        queryset = queryset.filter(lab=lab, name=name, reference=reference, is_active=True)
    elif lab and reference and trademark:
        queryset = queryset.filter(lab=lab, reference=reference, trademark=trademark, is_active=True)
    elif name and reference and trademark:
        queryset = queryset.filter(name=name, reference=reference, trademark=trademark, is_active=True)
    elif lab and name:
        queryset = queryset.filter(lab=lab, name=name, is_active=True)
    elif lab and trademark:
        queryset = queryset.filter(lab=lab, trademark=trademark, is_active=True)
    elif lab and reference:
        queryset = queryset.filter(lab=lab, reference=reference, is_active=True)
    elif name and reference:
        queryset = queryset.filter(name=name, reference=reference, is_active=True)
    elif name and trademark:
        queryset = queryset.filter(name=name, trademark=trademark, is_active=True)
    elif reference and trademark:
        queryset = queryset.filter(reference=reference, trademark=trademark, is_active=True)
    elif lab:
        queryset = queryset.filter(lab=lab, is_active=True)
    elif name:
        queryset = queryset.filter(name=name, is_active=True)
    elif trademark:
        queryset = queryset.filter(trademark=trademark, is_active=True)
    elif reference:
        queryset = queryset.filter(reference=reference, is_active=True)
    else:
        queryset = queryset.filter(is_active=True)

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
    sheet['F4'] = 'Referencia'
    sheet['G4'] = 'Unidad'
    sheet['H4'] = 'Ubicación'
    sheet['I4'] = 'Laboratorio'
    sheet['J4'] = 'Vencimiento'

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

    # Establecer el ancho de la columna G a 10
    sheet.column_dimensions['G'].width = 10

    # Establecer el ancho de la columna H a 12
    sheet.column_dimensions['H'].width = 12

    # Establecer el ancho de la columna I a 14
    sheet.column_dimensions['I'].width = 14

    # Establecer el ancho de la columna J a 13
    sheet.column_dimensions['J'].width = 13

    row = 4
    # Aplicar el estilo de borde a las celdas de la fila actual
    for col in range(1, 11):
        sheet.cell(row=row, column=col).border = thin_border
        sheet.cell(row=row, column=col).font = bold_font

    row = 5
    for item in queryset:
        sheet.cell(row=row, column=1).value = item.name.code
        sheet.cell(row=row, column=2).value = item.name.cas
        sheet.cell(row=row, column=3).value = item.name.name
        sheet.cell(row=row, column=4).value = item.trademark.name
        sheet.cell(row=row, column=5).value = item.reference
        sheet.cell(row=row, column=6).value = item.weight
        sheet.cell(row=row, column=7).value = item.unit.name
        sheet.cell(row=row, column=8).value = item.wlocation.name
        sheet.cell(row=row, column=9).value = item.lab.name
        sheet.cell(row=row, column=10).value = item.edate

        # Aplicar el estilo de borde a las celdas de la fila actual
        for col in range(1, 11):
            sheet.cell(row=row, column=col).border = thin_border

        row += 1

    # Obtén el rango de las columnas de la tabla
    start_column = 1
    end_column = 10
    start_row = 4
    end_row = row - 1

    # Convertir los números de las columnas en letras de columna
    start_column_letter = get_column_letter(start_column)
    end_column_letter = get_column_letter(end_column)

    # Rango de la tabla con el formato "A4:I{n}", donde n es el número de filas en la tabla
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

# Utilizando los valores filtrados en el template inventario.html, y guardados en los datos de sesión, se crea el archivo PDF 
# correspondiente e se introducen los valores desde la tabla del modelo Inventarios. Además, se aplican formatos a los encabezados, se 
# coloca un título, la fecha de creación y el logo. También se ajustan los anchos de columna y las alturas de fila
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

# Toma los valores enviados desde el template registrar_entrada.html o registrar_salida.html, consulta en la tabla reactivos y devuelve
# los valores de code, cas, state, y unit, para que se actualicen en los campos de entrada de los formualrios correspondientes
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

# Devuelve los valores de la tabla Reactivos según lo escrito en el campo name del formulario registrar_salida.html en forma de una 
# lista de autocompletado
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


# Devuelve los valores de la tabla Inventarios según lo escrito en el campo name del formulario registrar_salida.html en forma de una 
# lista de autocompletado
class AutocompleteOutAPI(View):
    def get(self, request):
        term = request.GET.get('term', '')
        lab = request.GET.get('lab', '')
       
        inventarios = Inventarios.objects.filter(
            Q(name__name__icontains=term) | Q(name__code__icontains=term) | Q(name__cas__icontains=term),
            lab__name__icontains=lab
        ).order_by('name').distinct('name')[:10]

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

# Devuelve los valores de la tabla Ubicaciones según lo escrito en el campo name del formulario registrar_salida.html en forma de 
# una lista de autocompletado
def autocomplete_location(request):
    term = request.GET.get('term', '')
    ubicaciones = Ubicaciones.objects.filter(Q(name__icontains=term))[:10]
    results = []
    for ubicacion in ubicaciones:
        results.append({'value': ubicacion.name})
    pass

    return JsonResponse(results, safe=False)

# Devuelve los valores de la tabla Responsables según lo escrito en el campo name del formulario registrar_salida.html en forma de 
# una lista de autocompletado
def autocomplete_manager(request):
    term = request.GET.get('term', '')
    responsables = Responsables.objects.filter(Q(name__icontains=term))[:10]
    results = []
    for responsable in responsables:
        results.append({'value': responsable.name})
    pass

    return JsonResponse(results, safe=False)

from django.http import JsonResponse


def obtener_stock(request):
    if request.method == "GET":
        lab_name = request.GET.get("lab")
        name = request.GET.get("name")
        trademark = request.GET.get("trademark")
        reference = request.GET.get("reference")
        
        # Obtener los IDs correspondientes a partir de los nombres
        lab = get_object_or_404(Laboratorios, name=lab_name)
        reactivos = get_object_or_404(Reactivos, name=name)
        
        # Realizar la lógica para obtener el stock en base a los parámetros recibidos

        # Supongamos que obtienes el stock de la base de datos o de alguna otra fuente de datos
        stock = Inventarios.objects.filter(lab=lab, name=reactivos, trademark=trademark, reference=reference).values("weight").first()
       
        # Devolver la respuesta en formato JSON
        return JsonResponse({"stock": stock})
