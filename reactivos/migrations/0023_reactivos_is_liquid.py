# Generated by Django 4.2 on 2023-04-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0022_remove_reactivos_density_reactivos_cas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactivos',
            name='is_liquid',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]