# Generated by Django 4.2.3 on 2023-10-24 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0033_configuracionsistema_tiempo_vencimiento_reactivos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del tipo de evento')),
            ],
            options={
                'verbose_name': 'Tipo de evento',
                'verbose_name_plural': 'Tipos de eventos',
            },
        ),
    ]
