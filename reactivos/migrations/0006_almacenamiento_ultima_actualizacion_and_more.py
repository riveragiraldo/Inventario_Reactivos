# Generated by Django 4.2.2 on 2023-07-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0005_almacenamiento_user_destinos_user_entradas_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacenamiento',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='destinos',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='estados',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='facultades',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='laboratorios',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='marcas',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='reactivos',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='respelc',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='responsables',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='salidas',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='sga',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='ubicaciones',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AddField(
            model_name='unidades',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última Actualización'),
        ),
        migrations.AlterField(
            model_name='almacenamiento',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='estados',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='facultades',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='inventarios',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Registro'),
        ),
        migrations.AlterField(
            model_name='laboratorios',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='reactivos',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='respelc',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='responsables',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='salidas',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='sga',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='unidades',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro'),
        ),
    ]
