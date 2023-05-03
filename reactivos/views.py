from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import *
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db import IntegrityError

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
            messages.error(request, 'Ya existe un reactivo con este nombre.')
            return redirect('reactivos:crear_reactivo')

        if Reactivos.objects.filter(code=code).exists():
            messages.error(request, 'Ya existe un reactivo con este código.')
            return redirect('reactivos:crear_reactivo')

        if Reactivos.objects.filter(cas=cas).exists():
            messages.error(request, 'Ya existe un reactivo con este número CAS.')
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

        messages.success(request, 'El reactivo se ha creado correctamente.')
        return redirect('reactivos:crear_reactivo')

    context={
        'unidades':Unidades.objects.all()
    }
    return render(request, 'reactivos/crear_reactivo.html', context)





def crear_unidad(request):
    if request.method=='POST':
        name = request.POST.get('name')

        unidad = Unidades.objects.create(
            
            name = name,
            
        )
        #return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

    context={
        
    }
    return render(request, 'reactivos/crear_unidad.html', context)



def crear_marca(request):
    if request.method=='POST':
        name = request.POST.get('name')

        marca = Marcas.objects.create(
            
            name = name,
            
        )
        #return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

    context={
        
    }
    return render(request, 'reactivos/crear_marca.html', context)


def crear_destino(request):
    if request.method=='POST':
        name = request.POST.get('name')

        destino = Destinos.objects.create(
            
            name = name,
            
        )
        #return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

    context={
        
    }
    return render(request, 'reactivos/crear_destino.html', context)


def crear_asignatura(request):
    if request.method=='POST':
        name = request.POST.get('name')

        asignatura = Asignaturas.objects.create(
            
            name = name,
            
        )
        #return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

    context={
        
    }
    return render(request, 'reactivos/crear_asignatura.html', context)

def crear_responsable(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')

        responsable = Responsables.objects.create(
            
            name = name,
            phone = phone,
            mail = mail,
            
        )
        #return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

    context={
        
    }
    return render(request, 'reactivos/crear_responsable.html', context)


def registrar_salida(request):
    error_message = ""
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        try:
            nameReactivo = Reactivos.objects.get(name=name)
            name = nameReactivo
        except Reactivos.DoesNotExist:
            error_message = "El reactivo ingresado no se encuentra en la base de datos."
            name = None

        if name:
            trademark = request.POST.get('trademark')
            trademark = Marcas.objects.get(id=trademark)
            reference = request.POST.get('reference')
            is_liquid = request.POST.get('is_liquid')
            weight = request.POST.get('weight')
            location = request.POST.get('location')
            destination = request.POST.get('destination')
            destination = Destinos.objects.get(id=destination)
            schoolsubject = request.POST.get('schoolsubject')
            schoolsubject = Asignaturas.objects.get(id=schoolsubject)
            manager = request.POST.get('manager')
            manager = Responsables.objects.get(id=manager)
            observations = request.POST.get('observations')

            salida = Salidas.objects.create(
                date=date,
                name=name,
                trademark=trademark,
                reference=reference,
                is_liquid=is_liquid,
                weight=weight,
                location=location,
                destination=destination,
                schoolsubject=schoolsubject,
                manager=manager,
                observations=observations,
            )

    context = {
        'reactivos': Reactivos.objects.all(),
        'destinos': Destinos.objects.all(),
        'responsables': Responsables.objects.all(),
        'asignaturas': Asignaturas.objects.all(),
        'marcas': Marcas.objects.all(),
        'error_message': error_message
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


