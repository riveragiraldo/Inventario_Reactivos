# Generated by Django 4.2 on 2023-04-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0011_alter_reactivos_subnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactivos',
            name='subnumber',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]