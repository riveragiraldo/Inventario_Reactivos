# Generated by Django 4.2.3 on 2023-09-22 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0010_rename_inventarios_entradas_inventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='salidas',
            name='inventario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='reactivos.inventarios', verbose_name='Id_Inventario'),
        ),
    ]
