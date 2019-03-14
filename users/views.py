from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


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