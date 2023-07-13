# Generated by Django 4.2.2 on 2023-07-12 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0003_responsables_cc_alter_user_email_alter_user_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ubicacion', to='reactivos.ubicaciones', verbose_name='Asignatura/Ubicación'),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Peso Reactivo'),
        ),
        migrations.AlterField(
            model_name='salidas',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Peso Reactivo'),
        ),
    ]