# Generated by Django 4.2 on 2023-04-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0006_reactive_is_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reactive',
            new_name='Reactivos',
        ),
        migrations.RenameModel(
            old_name='Unity',
            new_name='Unidades',
        ),
        migrations.AlterModelOptions(
            name='reactivos',
            options={'verbose_name_plural': 'Reactivos'},
        ),
        migrations.AlterModelOptions(
            name='unidades',
            options={'verbose_name_plural': 'Unidades'},
        ),
    ]