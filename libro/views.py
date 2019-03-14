from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import proyect
from .forms import Proyect_model_form
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

class proyect_create_view(LoginRequiredMixin,CreateView):
    template_name = 'agregar_proyecto.html'
    form_class = Proyect_model_form
    queryset = proyect.objects.all() 
    login_url = '/users/login/'   

    def post(self,request, *args, **kwargs):
        form = Proyect_model_form(request.POST)        
        if form.is_valid():
            print(request.user)
            form.instance.usuario = request.user
            folio_inicial = form.data['folio_inicial']
            form.instance.folio_final = int(folio_inicial) + (int(form.data['no_formatos'])-1)            
            messages.success(request, "Registro creado correctamente")
            form.save()
            return redirect(reverse("libro:proyect-detail", kwargs={"id":form.instance.id} ) )                              
        context = {"form":form}
        return render(request, self.template_name,context)
    
class proyect_update_view(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    template_name = 'agregar_proyecto.html'
    form_class = Proyect_model_form
    login_url = '/users/login/'
    # queryset = proyect.objects.all()  
    success_message = "Registro actualizado exitosamente"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(proyect, id=id_)
    
    def post(self,request, *args, **kwargs):
        form = Proyect_model_form(request.POST)        
        if form.is_valid():
            print(request.user)
            form.instance.usuario = request.user
            folio_inicial = form.data['folio_inicial']
            form.instance.folio_final = int(folio_inicial) + (int(form.data['no_formatos'])-1)            
            messages.success(request, "Registro creado correctamente")
            form.save()
            return redirect(reverse("libro:proyect-detail", kwargs={"id":form.instance.id} ) )                              
        context = {"form":form}
        return render(request, self.template_name,context)
  
class proyect_list_view(LoginRequiredMixin,ListView):
    template_name = 'lista_proyectos.html' 
    login_url = '/users/login/'

    def get_queryset(self):
        query = self.request.GET.get('q')        
        if query:
            queryset_list = proyect.objects.filter(
                Q(folio_inicial__icontains=query)|
                Q(titular__icontains=query)
                ).distinct()
            return queryset_list  
        query = proyect.objects.all()         
        return query

class proyect_detail_view(LoginRequiredMixin,DetailView):
    template_name = 'proyecto_detalles.html'
    login_url = '/users/login/'
    #queryset = proyect.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(proyect, id=id_)  

class proyect_delete_view(LoginRequiredMixin,DeleteView):   
    model = proyect
    success_url = reverse_lazy('libro:proyect-list')
    login_url = '/users/login/'
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(proyect, id=id_)



   
