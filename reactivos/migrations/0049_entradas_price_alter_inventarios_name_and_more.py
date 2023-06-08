# Generated by Django 4.2.2 on 2023-06-08 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0048_alter_responsables_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradas',
            name='price',
            field=models.IntegerField(default=50000, verbose_name='Valor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventarios',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactivos.reactivos', verbose_name='Nombre del reactivo'),
        ),
        migrations.AlterField(
            model_name='inventarios',
            name='trademark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactivos.marcas', verbose_name='Marca'),
        ),
    ]
