# Generated by Django 4.2.2 on 2023-07-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0005_alter_inventarios_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='price',
            field=models.BigIntegerField(verbose_name='Valor'),
        ),
    ]
