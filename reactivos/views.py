from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from .models import *
from django.db.models import Q
from django.contrib import messages


def index(request):
    unidades=Unidades.objects.all()
    reactivos=Reactivos.objects.all()
    context={
        'unidades':unidades,
        'reactivos':reactivos
    }
    return render(request, 'reactivos/index.html', context)


def detalle_reactivo(request, pk):
    
    reactivo = get_object_or_404(Reactivos, pk=pk)
    context={
        
        'reactivo':reactivo
    }
    return render(request, 'reactivos/detalle_reactivo.html', context)

def crear_reactivo(request):
    
    context = {
        'unidades': Unidades.objects.all(),
        
    }
    return render(request, 'reactivos/crear_reactivo.html', context)

def crear_reactivo_confirm(request):
    if request.method=='POST':
        color = request.POST.get('color')
        number = request.POST.get('number')
        number = str(number).zfill(3)
        subnumber=request.POST.get('subnumber')

        if subnumber=='':
            subnumber = '0'

        code = request.POST.get('code')
        name = request.POST.get('name')
        
        
        cas = request.POST.get('cas')
        wlocation = request.POST.get('wlocation')
        is_liquid = request.POST.get('is_liquid')

        unit = request.POST.get('unit')
        nUnit=unit
        
        try:
            nameUnit = Unidades.objects.get(name=unit)
            unit = nameUnit
        except Unidades.DoesNotExist:
            messages.error(request,"La Unidad "+nUnit+" no se encuentra en la base de datos, favor crearlo primero.") 
            unit = None
            return redirect('reactivos:crear_reactivo_confirm')
        
        # Verifica si ya existe un registro con el mismo nombre, código o número CAS
        if Reactivos.objects.filter(name=name).exists():
            reactivo=Reactivos.objects.get(name=name)
            reactivo_name=reactivo.name
            messages.error(request, 'Ya existe un reactivo con el nombre registrado: '+reactivo_name)
            return redirect('reactivos:crear_reactivo_confirm')

        if Reactivos.objects.filter(code=code).exists():
            reactivo=Reactivos.objects.get(code=code)
            reactivo_name=reactivo.name
            messages.error(request, 'Ya existe un reactivo con el código registrado: '+reactivo_name)
            return redirect('reactivos:crear_reactivo_confirm')

        if Reactivos.objects.filter(cas=cas).exists():
            reactivo=Reactivos.objects.get(cas=cas)
            reactivo_name=reactivo.name
            messages.error(request, 'Ya existe un reactivo con el CAS registrado: '+reactivo_name)
            return redirect('reactivos:crear_reactivo_confirm')

        reactivo = Reactivos.objects.create(
            color = color,
            number = number,
            subnumber = subnumber,
            code = code,
            name = name,
            unit = unit,
            cas = cas,
            wlocation=wlocation,
            is_liquid=is_liquid,
        )

        messages.success(request, 'Se ha creado exitosamente el reactivo: '+name)
        return redirect('reactivos:crear_reactivo_confirm')

    context={
        'unidades':Unidades.objects.all()
    }
    return render(request, 'reactivos/crear_reactivo_confirm.html', context)





def crear_unidad(request):
    if request.method=='POST':
        name = request.POST.get('name')
        

        # Verifica si ya existe un registro con el mismo nombre de la unidad
        if Unidades.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe una unidad con nombre: '+name)
            return redirect('reactivos:crear_unidad')

        

        unidad = Unidades.objects.create(
            
            name = name,
            
        )
        messages.success(request, 'Se ha creado exitosamente la unidad con nombre: '+name+'.')
        return redirect('reactivos:crear_unidad')

    context={
        
    }
    return render(request, 'reactivos/crear_unidad.html', context)



def crear_unidades(request):
    if request.method=='POST':
        name = request.POST.get('name')
        
        # Verifica si ya existe un registro con el mismo nombre de la unidad
        if Unidades.objects.filter(name=name).exists():
            unidad=Unidades.objects.get(name=name)
            unidad_id=unidad.id
            messages.error(request, 'Ya existe una unidad con nombre '+name+' id: '+str(unidad_id))
            return redirect('reactivos:crear_unidades')

        unidad = Unidades.objects.create(
            name=name,
        )
        unidad_id=unidad.id
        
        messages.success(request, 'Se ha creado exitosamente la unidad con nombre '+name+' id: '+str(unidad_id))
        
        # Agregar el ID de la unidad al contexto para seleccionarla en la plantilla
        context = {'unidad_id': unidad.id,'unidad_name': unidad.name,}
        return render(request, 'reactivos/crear_unidades.html', context)

    context={
        
    }
    return render(request, 'reactivos/crear_unidades.html', context)


def crear_marca(request):
    if request.method=='POST':
        name = request.POST.get('name')
        # Verifica si ya existe un registro con el mismo nombre de la marca
        if Marcas.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe una marca con nombre: '+name)
            return redirect('reactivos:crear_marca')

        marca = Marcas.objects.create(
            
            name = name,
            
        )
        messages.success(request, 'Se ha creado exitosamente la marca con nombre: '+name+'.')
        return redirect('reactivos:crear_marca')

    context={
        
    }
    return render(request, 'reactivos/crear_marca.html', context)

def crear_marcas(request):
    if request.method=='POST':
        name = request.POST.get('name')
        
        # Verifica si ya existe un registro con el mismo nombre de la marca
        if Marcas.objects.filter(name=name).exists():
            marca=Marcas.objects.get(name=name)
            marca_id=marca.id
            messages.error(request, 'Ya existe una marca con nombre '+name+' id: '+str(marca_id))
            return redirect('reactivos:crear_marcas')

        marca = Marcas.objects.create(
            
            name = name,
            
        )
        marca_id=marca.id
        messages.success(request, 'Se ha creado exitosamente la marca con nombre '+name+' id: '+str(marca_id))
        return redirect('reactivos:crear_marcas')

    context={
        
    }
    return render(request, 'reactivos/crear_marcas.html', context)



def crear_destino(request):
    if request.method=='POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre del destino
        if Destinos.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe un destino con nombre: '+name)
            return redirect('reactivos:crear_destino')


        destino = Destinos.objects.create(
            
            name = name,
            
        )
        messages.success(request, 'Se ha creado exitosamente el destino con nombre: '+name+'.')
        return redirect('reactivos:crear_destino')

    context={
        
    }
    return render(request, 'reactivos/crear_destino.html', context)

def crear_destinos(request):
    if request.method=='POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre del destino
        if Destinos.objects.filter(name=name).exists():
            destino=Destinos.objects.get(name=name)
            destino_id=destino.id
            messages.error(request, 'Ya existe un destino llamado '+name+' con id: '+str(destino_id))
            return redirect('reactivos:crear_destinos')


        destino = Destinos.objects.create(
            
            name = name,
            
        )
        destino_id=destino.id
        messages.success(request, 'Se ha creado exitosamente el destino con nombre '+name+' con id: '+str(destino_id))
        return redirect('reactivos:crear_destinos')

    context={
        
    }
    return render(request, 'reactivos/crear_destinos.html', context)


def crear_ubicacion(request):
    if request.method=='POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre de la asignatura
        if Ubicaciones.objects.filter(name=name).exists():
            
            messages.error(request, 'Ya existe una ubicación con nombre: '+name)
            return redirect('reactivos:crear_ubicacion')

        asignatura = Ubicaciones.objects.create(
            
            name = name,
            
        )
        messages.success(request, 'Se ha creado exitosamente la ubicación con nombre: '+name+'.')
        return redirect('reactivos:crear_ubicacion')
    context={
        
    }
    return render(request, 'reactivos/crear_ubicacion.html', context)

def crear_ubicaciones(request):
    if request.method=='POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre de la asignatura
        if Ubicaciones.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe una ubicación con nombre: '+name)
            return redirect('reactivos:crear_ubicaciones')

        ubicacion = Ubicaciones.objects.create(
            
            name = name,
            
        )
        
        messages.success(request, 'Se ha creado exitosamente la ubicación: '+name)
        return redirect('reactivos:crear_ubicaciones')
    context={
        
    }
    return render(request, 'reactivos/crear_ubicaciones.html', context)


def crear_responsable(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')

        

        # Verifica si ya existe un registro con el mismo nombre, telefono o email de la marca
        if Responsables.objects.filter(name=name).exists():
            responsablename=Responsables.objects.get(name=name)
            responsable_name=responsablename.name
            messages.error(request, 'Ya existe una responsable con nombre: '+responsable_name)
            return redirect('reactivos:crear_responsable')
        
        if Responsables.objects.filter(phone=phone).exists():
            responsablename=Responsables.objects.get(phone=phone)
            responsable_name=responsablename.name
            messages.error(request, 'Ya existe una responsable con el telefono registrado: '+responsable_name)
            return redirect('reactivos:crear_responsable')
        
        if Responsables.objects.filter(mail=mail).exists():
            responsablename=Responsables.objects.get(mail=mail)
            responsable_name=responsablename.name
            messages.error(request, 'Ya existe una responsable con el email registrado: '+responsable_name)
            return redirect('reactivos:crear_responsable')

        responsable = Responsables.objects.create(
            
            name = name,
            phone = phone,
            mail = mail,
            
        )
        messages.success(request, 'Se ha creado exitosamente el siguiente responsable: '+name)
        return redirect('reactivos:crear_responsable')

    context={
        
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
        date = request.POST.get('date')
        name = request.POST.get('name')
        nReactivo=name
        try:
            nameReactivo = Reactivos.objects.get(name=name)
            name = nameReactivo
        except Reactivos.DoesNotExist:
            messages.error(request,"El reactivo "+nReactivo+" no se encuentra en la base de datos, favor crearlo primero.") 
            name = None
            return redirect('reactivos:registrar_salida_confirm')
        
        location = request.POST.get('location')
        nlocation=location
        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation
        except Ubicaciones.DoesNotExist:
            messages.error(request,"La ubicación "+nlocation+" no se encuentra en la base de datos, favor crearlo primero.") 
            location = None
            return redirect('reactivos:registrar_salida_confirm')
        
        manager = request.POST.get('manager')
        nmanager=manager
        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request,"El responsable "+nmanager+" no se encuentra en la base de datos, favor crearlo primero.") 
            manager = None
            return redirect('reactivos:registrar_salida_confirm')
        
        trademark = request.POST.get('trademark')
        nMarca=trademark
        
        try:
            nameMarca = Marcas.objects.get(name=trademark)
            trademark = nameMarca
        except Marcas.DoesNotExist:
            messages.error(request,"La marca "+nMarca+" no se encuentra en la base de datos, favor crearlo primero.") 
            trademark = None
            return redirect('reactivos:registrar_salida_confirm')
        
        destination = request.POST.get('destination')
        nDestino=destination
        
        try:
            nameDestino = Destinos.objects.get(name=destination)
            destination = nameDestino
        except Marcas.DoesNotExist:
            messages.error(request,"El destino "+nDestino+" no se encuentra en la base de datos, favor crearlo primero.") 
            destination = None
            return redirect('reactivos:registrar_salida_confirm')
        
        
        
        if name:
            

            reference = request.POST.get('reference')
            is_liquid = request.POST.get('is_liquid')
            weight = request.POST.get('weight')
            observations = request.POST.get('observations')
            unit=request.POST.get('unit')


            

            salida = Salidas.objects.create(
                date=date,
                name=name,
                trademark=trademark,
                reference=reference,
                is_liquid=is_liquid,
                weight=weight,
                location=location,
                destination=destination,
                manager=manager,
                observations=observations,
                )       
            messages.success(request, 'Se ha registrado de manera exitosa la salida del insumo: '+nReactivo+', cantidad '+weight+' '+unit)
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
        date = request.POST.get('date')
        name = request.POST.get('name')
        nReactivo=name
        try:
            nameReactivo = Reactivos.objects.get(name=name)
            name = nameReactivo
        except Reactivos.DoesNotExist:
            messages.error(request,"El reactivo "+nReactivo+" no se encuentra en la base de datos, favor crearlo primero.") 
            name = None
            return redirect('reactivos:registrar_entrada_confirm')
        
        location = request.POST.get('location')
        nlocation=location
        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation
        except Ubicaciones.DoesNotExist:
            messages.error(request,"La ubicación "+nlocation+" no se encuentra en la base de datos, favor crearlo primero.") 
            location = None
            return redirect('reactivos:registrar_entrada_confirm')
        
        manager = request.POST.get('manager')
        nmanager=manager
        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request,"El responsable "+nmanager+" no se encuentra en la base de datos, favor crearlo primero.") 
            manager = None
            return redirect('reactivos:registrar_entrada_confirm')
        
        trademark = request.POST.get('trademark')
        nMarca=trademark
        
        try:
            nameMarca = Marcas.objects.get(name=trademark)
            trademark = nameMarca
        except Marcas.DoesNotExist:
            messages.error(request,"La marca "+nMarca+" no se encuentra en la base de datos, favor crearlo primero.") 
            trademark = None
            return redirect('reactivos:registrar_entrada_confirm')
        
        if name:
            
            reference = request.POST.get('reference')
            is_liquid = request.POST.get('is_liquid')
            weight = request.POST.get('weight')
            
            order = request.POST.get('order')
            
            
            
            observations = request.POST.get('observations')
            unit=request.POST.get('unit')


            

            salida = Entradas.objects.create(
                date=date,
                name=name,
                trademark=trademark,
                reference=reference,
                is_liquid=is_liquid,
                weight=weight,
                location=location,
                order=order,
                manager=manager,
                observations=observations,
                )       
            messages.success(request, 'Se ha registrado de manera exitosa el ingreso del insumo del insumo: '+nReactivo+', cantidad '+weight+' '+unit)
            return redirect('reactivos:registrar_entrada_confirm')       
           

    context = {
        'reactivos': Reactivos.objects.all(),
        'responsables': Responsables.objects.all(),
         'marcas': Marcas.objects.all(),
        'ubicaiones': Ubicaciones.objects.all()
    }
    return render(request, 'reactivos/registrar_entrada_confirm.html', context)









def get_value(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Si la solicitud es una solicitud AJAX, procesar la solicitud y devolver una respuesta JSON
        value_selected = request.GET.get('value_selected')
        try:
            # Intentar obtener el valor correspondiente de la base de datos
            reactivo = Reactivos.objects.get(name=value_selected)
            cas = reactivo.cas
            codigo = reactivo.code
            liquid = reactivo.is_liquid
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
    reactivos = Reactivos.objects.filter(Q(name__icontains=term) | Q(code__icontains=term) | Q(cas__icontains=term))[:10]
    results = []
    for reactivo in reactivos:
        results.append({'id': reactivo.id, 'value': reactivo.name})

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



