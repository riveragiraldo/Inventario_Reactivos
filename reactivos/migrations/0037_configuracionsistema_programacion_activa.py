# Generated by Django 4.2.3 on 2023-10-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0036_alter_eventos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracionsistema',
            name='programacion_activa',
            field=models.BooleanField(default=False, verbose_name='Activar / Desactivar programación'),
        ),
    ]
