# Generated by Django 4.2.3 on 2023-10-12 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0018_alter_reactivos_cas'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('is_active', models.BooleanField(default=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updateby_TipoS', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'Tipo de solicitud',
                'verbose_name_plural': 'Tipo de solicitud',
            },
        ),
    ]