# Generated by Django 4.2 on 2023-05-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0042_estados_alter_reactivos_is_liquid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactivos',
            name='is_liquid',
        ),
        migrations.AddField(
            model_name='reactivos',
            name='state',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='state', to='reactivos.estados', verbose_name='Presentación'),
            preserve_default=False,
        ),
    ]
