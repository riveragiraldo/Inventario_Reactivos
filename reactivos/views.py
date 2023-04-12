from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
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



