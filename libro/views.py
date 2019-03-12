from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import proyect
from .forms import Proyect_model_form
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)


class proyect_create_view(CreateView):
    template_name = 'agregar_proyecto.html'
    form_class = Proyect_model_form
    queryset = proyect.objects.all()    

    def post(self,request, *args, **kwargs):
        form = Proyect_model_form(request.POST)        
        if form.is_valid():
            print(request.user)
            form.instance.usuario = request.user
            folio_inicial = form.data['folio_inicial']
            form.instance.folio_final = int(folio_inicial) + (int(form.data['no_formatos'])-1)            
            form.save()
            return redirect(reverse("libro:proyect-detail", kwargs={"id":form.instance.id} ) )                              
        context = {"form":form}
        return render(request, self.template_name,context)
    

class proyect_update_view(UpdateView):
    template_name = 'agregar_proyecto.html'
    form_class = Proyect_model_form
    queryset = proyect.objects.all()  

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(proyect, id=id_)    

class proyect_list_view(ListView):
    template_name = 'lista_proyectos.html'
    queryset = proyect.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('q')        
        if query:
            queryset_list = proyect.objects.filter(
                Q(folio_inicial__icontains=query)|
                Q(titular__icontains=query)
                ).distinct()
            return queryset_list           
        return self.queryset

class proyect_detail_view(DetailView):
    template_name = 'proyecto_detalles.html'
    #queryset = proyect.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(proyect, id=id_)  

class proyect_delete_view(DeleteView):   
    model = proyect
    success_url = reverse_lazy('libro:proyect-list')
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(proyect, id=id_)

class proyect_search_view(ListView):
    template_name = 'lista_proyectos.html'    

   
