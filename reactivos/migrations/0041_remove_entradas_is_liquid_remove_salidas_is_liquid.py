# Generated by Django 4.2 on 2023-05-24 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0040_alter_entradas_options_remove_reactivos_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradas',
            name='is_liquid',
        ),
        migrations.RemoveField(
            model_name='salidas',
            name='is_liquid',
        ),
    ]
