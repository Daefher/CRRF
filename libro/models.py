from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class proyect(models.Model):
    folio_inicial = models.CharField(max_length=128, null=True)
    folio_final = models.CharField(max_length=128, null=True, blank=True)
    no_formatos = models.IntegerField(null=True)
    volumen = models.IntegerField(null=True)
    unidad_de_medida = models.CharField(max_length=8, null=True)
    especie = models.CharField(max_length=64, null=True)
    producto = models.CharField(max_length=64, null=True)
    titular = models.CharField(max_length=128, null=True,default=None)
    #TODO:Revisar esto para que tome la fechas en formato dia/mes/año
    fecha = models.DateField(null=True)
    no_oficio = models.CharField(max_length=128, null=True)
    vigencia = models.DateField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self, *args, **kwargs):
        return self.titular

    #TODO:Modificar esto para mandar al proyecto que se agregue
    def get_absolute_url(self):
        return reverse("libro:proyect-detail", kwargs={"id":self.id} )