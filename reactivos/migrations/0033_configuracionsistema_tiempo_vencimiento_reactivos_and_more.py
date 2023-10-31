# Generated by Django 4.2.3 on 2023-10-24 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0032_alter_inventarios_edate'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracionsistema',
            name='tiempo_vencimiento_reactivos',
            field=models.PositiveIntegerField(default=90, verbose_name='Tiempo para verificar vencimiento de reactivos (días)'),
        ),
        migrations.AlterField(
            model_name='configuracionsistema',
            name='tiempo_eventos',
            field=models.PositiveIntegerField(default=90, verbose_name='Tiempo para depuración de eventos (días)'),
        ),
        migrations.AlterField(
            model_name='configuracionsistema',
            name='tiempo_solicitudes',
            field=models.PositiveIntegerField(default=90, verbose_name='Tiempo para depuración de solicitudes (días)'),
        ),
    ]