from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('agregar/',views.create_user_view.as_view(), name="register"),
    path('usuarios/',views.user_list_view.as_view(), name='user-list'),
    
]