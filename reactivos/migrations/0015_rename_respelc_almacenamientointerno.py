# Generated by Django 4.2.3 on 2023-10-10 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0014_alter_clasealmacenamiento_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RespelC',
            new_name='AlmacenamientoInterno',
        ),
    ]