# Generated by Django 4.1.2 on 2022-11-06 14:49

import datetime
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
            name='Expensa',
            fields=[
                ('IdExpensa', models.AutoField(primary_key=True, serialize=False)),
                ('anio', models.CharField(max_length=4, verbose_name='Año')),
                ('mes', models.CharField(max_length=2, verbose_name='Mes')),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe')),
                ('pagado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Pagado')),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha')),
                ('fechapago', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('IdUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.PositiveSmallIntegerField(unique=True, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=35, verbose_name='Apellido')),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('numero', models.CharField(max_length=5, verbose_name='Número')),
                ('piso', models.CharField(max_length=2, verbose_name='Piso')),
                ('dpto', models.CharField(max_length=3, verbose_name='Departamento')),
                ('observacion', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observación')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
