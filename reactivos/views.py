from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import *

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
        number = '00'+number
        subnumber=request.POST.get('subnumber')
        
        if subnumber=='' :
            subnumber = '0'
            code = color+'-'+number
        else:
            code = color+'-'+number+'-'+subnumber
            
        name = request.POST.get('name')
        unit = request.POST.get('unit')
        unit = Unidades.objects.get(id=unit)
        density = request.POST.get('density')
        if density=='':
            density = '0'

        reactivo = Reactivos.objects.create(
            color = color,
            number = number,
            subnumber = subnumber,
            code = code,
            name = name,
            unit = unit,
            density = density,
            
        )
        return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

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
    if request.method=='POST':
        date = request.POST.get('date')
        reference = request.POST.get('reference')
        weight = request.POST.get('weight')
        
        is_liquid = request.POST.get('is_liquid')
        observations = request.POST.get('observations')
        

        if is_liquid==True:
            density = request.POST.get('name')
            density = Reactivos.objects.get(id=density)
        else:
            density=1

        if is_liquid==True:
            out_reagent=density*weight
        else:
            out_reagent=weight
        
        destination = request.POST.get('destination')
        destination = Destinos.objects.get(id=destination)
        manager = request.POST.get('manager')
        manager = Responsables.objects.get(id=manager)
        name = request.POST.get('name')
        name = Responsables.objects.get(id=name)
        schoolsubject = request.POST.get('schoolsubject')
        schoolsubject = Responsables.objects.get(id=schoolsubject)
        trademark = request.POST.get('trademark')
        trademark = Marcas.objects.get(id=trademark)
        observations = request.POST.get('observations')


        salida = Salidas.objects.create(
            date = date,
            reference = reference,
            weight = weight,
            is_liquid = is_liquid,
            observations = observations,
            out_reagent=out_reagent,
            destination = destination,
            manager = manager,
            name = name,
            schoolsubject = schoolsubject,
            trademark = trademark,
           
        )
        #return redirect('reactivos:detalle_reactivo', pk=reactivo.id)

    context={
        'reactivos':Reactivos.objects.all(),
        'destinos':Destinos.objects.all(),
        'responsables':Responsables.objects.all(),
        'asignatura':Asignaturas.objects.all(),
        'marcas':Marcas.objects.all(),


    }
    return render(request, 'reactivos/registrar_salida.html', context)





def get_value(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Si la solicitud es una solicitud AJAX, procesar la solicitud y devolver una respuesta JSON
        value_selected = request.GET.get('value_selected')
        try:
            # Intentar obtener el valor correspondiente de la base de datos
            reactivo = Reactivos.objects.get(id=value_selected)
            densidad = reactivo.density
            codigo= reactivo.code
        except Reactivos.DoesNotExist:
            # Si el reactivo no existe, devolver un valor por defecto
            value = 1

        return JsonResponse({'value': densidad,
                             'codigo':codigo
                             })
    else:
        # Si la solicitud no es una solicitud AJAX, devolver una respuesta HTTP 400 Bad Request
        return HttpResponseBadRequest()
