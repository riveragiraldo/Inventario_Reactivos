# Generated by Django 5.0.1 on 2024-02-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0013_alter_solicitudesexternas_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracionsistema',
            name='url',
            field=models.CharField(blank=True, default='https://manizales.unal.edu.co/', max_length=500, null=True, verbose_name='Url'),
        ),
    ]