# Generated by Django 4.2 on 2023-05-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0029_alter_ubicaciones_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicaciones',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Ubicación/Asignaturas'),
        ),
    ]
