# Generated by Django 4.2 on 2023-04-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0010_alter_reactivos_subnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactivos',
            name='subnumber',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
