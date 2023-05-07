# Generated by Django 4.2 on 2023-04-11 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reactivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.PositiveIntegerField(max_length=2)),
                ('number', models.PositiveIntegerField(max_length=2)),
                ('subnumber', models.PositiveIntegerField(max_length=2)),
                ('code', models.CharField(max_length=255)),
                ('density', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactivos.unity')),
            ],
        ),
    ]