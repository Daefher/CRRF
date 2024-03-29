# Generated by Django 2.1.7 on 2019-03-11 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='proyect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_inicial', models.CharField(max_length=128, null=True)),
                ('folio_final', models.CharField(max_length=128, null=True)),
                ('no_formatos', models.IntegerField(null=True)),
                ('volumen', models.IntegerField(max_length=64, null=True)),
                ('unidad_de_medida', models.CharField(max_length=8, null=True)),
                ('especie', models.CharField(max_length=64, null=True)),
                ('producto', models.CharField(max_length=64, null=True)),
                ('titular', models.CharField(max_length=128, null=True)),
                ('fecha', models.DateField(null=True)),
                ('no_oficio', models.CharField(max_length=128, null=True)),
                ('vigencia', models.DateField(null=True)),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
