# Generated by Django 4.2 on 2023-04-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0014_destinos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
            },
        ),
    ]
