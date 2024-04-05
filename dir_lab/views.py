from django.shortcuts import render
from django.views.generic import ListView, View, CreateView, UpdateView

# Create your views here.
# Vista para la creación del index Dirlab, 

class HomeDirLab(View):  # Utiliza LoginRequiredMixin como clase base
    template_name = 'dir_lab/index.html'  # Nombre de la plantilla

    def get(self, request,*args,**kwargs):
        
             
        context = {
            
        }
        return render(request, self.template_name, context)