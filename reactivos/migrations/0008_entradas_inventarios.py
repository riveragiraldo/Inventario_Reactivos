# Generated by Django 4.2.3 on 2023-09-18 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0007_alter_responsables_acceptdataprocessing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradas',
            name='inventarios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inv', to='reactivos.inventarios', verbose_name='Id_Inventario'),
            preserve_default=False,
        ),
    ]
