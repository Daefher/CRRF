from django.shortcuts import render,redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms  import AgregarForm

from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("libro:proyect-list")
    else:
        if request.user.is_authenticated:
            return redirect("libro:proyect-list")
        else:
            form = AuthenticationForm(request)
    return render(request, 'login.html', {'form':form})

def logout_view(request):    
    logout(request)
    return redirect('users:login')


class create_user_view(LoginRequiredMixin,CreateView):
    template_name = 'agregar_usuario.html'
    form_class = AgregarForm
    queryset = User.objects.all() 
    login_url = '/users/login/'

    def get_success_url(self):
        return '/libro/'

class user_list_view(LoginRequiredMixin, ListView):
    template_name = 'lista_usuarios.html' 
    login_url = '/users/login/'
    queryset = User.objects.all()

