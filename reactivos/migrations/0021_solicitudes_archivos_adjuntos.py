# Generated by Django 4.2.3 on 2023-10-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0020_solicitudes'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudes',
            name='archivos_adjuntos',
            field=models.FileField(blank=True, null=True, upload_to='archivos_solicitudes/'),
        ),
    ]