from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AgregarForm(UserCreationForm):
    class Meta:
        model = User
        fields = (  'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                 )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Opcional')
    