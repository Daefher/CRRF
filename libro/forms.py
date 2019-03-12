from django import forms
from .models import proyect


class Proyect_model_form(forms.ModelForm):
    class Meta:
        model = proyect
        fields = [
            'folio_inicial',
            'folio_final',            
            'no_formatos',
            'volumen',
            'unidad_de_medida',
            'especie',
            'producto',
            'titular',
            'fecha',
            'no_oficio',
            'vigencia'
        ]