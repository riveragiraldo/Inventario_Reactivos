# Generated by Django 4.2.3 on 2023-10-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0037_configuracionsistema_programacion_activa'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracionsistema',
            name='manual',
            field=models.FileField(blank=True, null=True, upload_to='manual/'),
        ),
    ]
