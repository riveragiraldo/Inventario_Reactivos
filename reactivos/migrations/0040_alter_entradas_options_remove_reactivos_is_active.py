# Generated by Django 4.2 on 2023-05-24 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0039_inventarios_unit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entradas',
            options={'verbose_name': 'Entrada', 'verbose_name_plural': 'Entradas'},
        ),
        migrations.RemoveField(
            model_name='reactivos',
            name='is_active',
        ),
    ]