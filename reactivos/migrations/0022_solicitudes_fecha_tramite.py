# Generated by Django 4.2.3 on 2023-10-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0021_solicitudes_archivos_adjuntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudes',
            name='fecha_tramite',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de trámite'),
        ),
    ]