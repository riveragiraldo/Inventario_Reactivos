from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import *
from django.db.models import Q
from django.contrib import messages
#from django.contrib.sessions.models import Session

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
    if request.method=='POST':
        color = request.POST.get('color')
        number = request.POST.get('number')
        number = str(number).zfill(3)
        subnumber=request.POST.get('subnumber')

        if subnumber=='':
            subnumber = '0'

        code = request.POST.get('code')
        name = request.POST.get('name')
        unit = request.POST.get('unit')
        unit = Unidades.objects.get(id=unit)
        cas = request.POST.get('cas')
        wlocation = request.POST.get('wlocation')
        is_liquid = request.POST.get('is_liquid')
        
        # Verifica si ya existe un registro con el mismo nombre, código o número CAS
        if Reactivos.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe un reactivo con nombre '+name)
            return redirect('reactivos:crear_reactivo')

        if Reactivos.objects.filter(code=code).exists():
            messages.error(request, 'Ya existe un reactivo con código '+code)
            return redirect('reactivos:crear_reactivo')

        if Reactivos.objects.filter(cas=cas).exists():
            messages.error(request, 'Ya existe un reactivo con  CAS '+cas)
            return redirect('reactivos:crear_reactivo')

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

        messages.success(request, 'Se ha creado exitosamente el reactivo con nombre: '+name+', CAS: '+cas+', código interno: '+code)
        return redirect('reactivos:crear_reactivo')

    context={
        'unidades':Unidades.objects.all()
    }
    return render(request, 'reactivos/crear_reactivo.html', context)





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


# def crear_unidades(request):
#     if request.method=='POST':
#         name = request.POST.get('name')

#         # Verifica si ya existe un registro con el mismo nombre de la unidad
#         if Unidades.objects.filter(name=name).exists():
#             messages.error(request, 'Ya existe una unidad con nombre: '+name)
#             return redirect('reactivos:crear_unidad')

        

#         unidad = Unidades.objects.create(
            
#             name = name,
            
#         )
#         messages.success(request, 'Se ha creado exitosamente la unidad con nombre: '+name+'.')
#         return redirect('reactivos:crear_unidades')

#     context={
        
#     }
#     return render(request, 'reactivos/crear_unidad.html', context)

def crear_unidades(request):
    if request.method=='POST':
        name = request.POST.get('name')

        # Verifica si ya existe un registro con el mismo nombre de la unidad
        if Unidades.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe una unidad con nombre: '+name)
            return redirect('reactivos:crear_unidades')

        unidad = Unidades.objects.create(
            name=name,
        )
        messages.success(request, 'Se ha creado exitosamente la unidad con nombre: '+name+'.')
        
        # Agregar el ID de la unidad al contexto para seleccionarla en la plantilla
        context = {'unidad_id': unidad.id,}
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


def crear_responsable(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')

        # Verifica si ya existe un registro con el mismo nombre, telefono o email de la marca
        if Responsables.objects.filter(name=name).exists():
            messages.error(request, 'Ya existe una responsable con nombre: '+name)
            return redirect('reactivos:crear_responsable')
        
        if Responsables.objects.filter(phone=phone).exists():
            messages.error(request, 'Ya existe una responsable con telefono: '+phone)
            return redirect('reactivos:crear_responsable')
        
        if Responsables.objects.filter(mail=mail).exists():
            messages.error(request, 'Ya existe una responsable con email: '+mail)
            return redirect('reactivos:crear_responsable')

        responsable = Responsables.objects.create(
            
            name = name,
            phone = phone,
            mail = mail,
            
        )
        messages.success(request, 'Se ha creado exitosamente el responsable con nombre: '+name+', teléfono: '+phone+', email: '+mail+'.')
        return redirect('reactivos:crear_responsable')

    context={
        
    }
    return render(request, 'reactivos/crear_responsable.html', context)


def registrar_salida(request):
    
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
            return redirect('reactivos:registrar_salida')
        
        location = request.POST.get('location')
        nlocation=location
        try:
            nameLocation = Ubicaciones.objects.get(name=location)
            location = nameLocation
        except Ubicaciones.DoesNotExist:
            messages.error(request,"La ubicación "+nlocation+" no se encuentra en la base de datos, favor crearlo primero.") 
            location = None
            return redirect('reactivos:registrar_salida')
        
        manager = request.POST.get('manager')
        nmanager=manager
        try:
            nameManager = Responsables.objects.get(name=manager)
            manager = nameManager
        except Responsables.DoesNotExist:
            messages.error(request,"El responsable "+nmanager+" no se encuentra en la base de datos, favor crearlo primero.") 
            manager = None
            return redirect('reactivos:registrar_salida')
            

        if name:
            trademark = request.POST.get('trademark')
            trademark = Marcas.objects.get(id=trademark)
            reference = request.POST.get('reference')
            is_liquid = request.POST.get('is_liquid')
            weight = request.POST.get('weight')
            
            destination = request.POST.get('destination')
            destination = Destinos.objects.get(id=destination)
            
            
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
            return redirect('reactivos:registrar_salida')

        
           

    context = {
        'reactivos': Reactivos.objects.all(),
        'destinos': Destinos.objects.all(),
        'responsables': Responsables.objects.all(),
         'marcas': Marcas.objects.all(),
        'ubicaiones': Ubicaciones.objects.all()
    }
    return render(request, 'reactivos/registrar_salida.html', context)









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



