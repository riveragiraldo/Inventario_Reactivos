# Generated by Django 4.2.2 on 2023-06-13 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Ubicación/Asignaturas')),
                ('description', models.TextField(max_length=1000, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Almacenamiento',
                'verbose_name_plural': 'Almacenamientos',
            },
        ),
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Destino')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Destino',
                'verbose_name_plural': 'Destinos',
            },
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('reference', models.CharField(max_length=255, verbose_name='Referencia')),
                ('weight', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Peso Reactivo')),
                ('order', models.CharField(max_length=255, verbose_name='Orden No.')),
                ('observations', models.TextField(max_length=1000, verbose_name='Observaciones')),
                ('price', models.IntegerField(verbose_name='Valor')),
                ('edate', models.DateField(verbose_name='Fecha de vencimiento')),
                ('nproject', models.CharField(max_length=15, verbose_name='Número de proyecto')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactivos.destinos', verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Estado')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Facultades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre Facultad')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='Inventarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Inventario Actual')),
                ('reference', models.CharField(max_length=20, verbose_name='Referencia')),
                ('fecha_registro', models.DateTimeField(auto_now=True, verbose_name='Últma actualización')),
            ],
            options={
                'verbose_name_plural': 'Inventarios',
            },
        ),
        migrations.CreateModel(
            name='Laboratorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre Laboratorio')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Laboratorio',
                'verbose_name_plural': 'Laboratorios',
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Marca')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Reactivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.PositiveIntegerField(verbose_name='Color CGA')),
                ('number', models.CharField(max_length=5, verbose_name='Número')),
                ('subnumber', models.CharField(max_length=3, verbose_name='Sub-número')),
                ('code', models.CharField(max_length=255, verbose_name='Código')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('cas', models.CharField(max_length=20, verbose_name='Código CAS')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reactivo',
                'verbose_name_plural': 'Reactivos',
            },
        ),
        migrations.CreateModel(
            name='RespelC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Clasificación Respel')),
                ('description', models.TextField(max_length=1000, verbose_name='Descripción')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Clasificaciones',
                'verbose_name_plural': 'Clasificación',
            },
        ),
        migrations.CreateModel(
            name='Responsables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre Responsable')),
                ('mail', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
            },
        ),
        migrations.CreateModel(
            name='Salidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('reference', models.CharField(max_length=255, verbose_name='Referencia')),
                ('weight', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Peso Reactivo')),
                ('observations', models.TextField(max_length=1000, verbose_name='Observaciones')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='reactivos.destinos', verbose_name='Destino')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab', to='reactivos.laboratorios', verbose_name='Laboratorio')),
            ],
            options={
                'verbose_name': 'Salida',
                'verbose_name_plural': 'Salidas',
            },
        ),
        migrations.CreateModel(
            name='SGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Código SGA')),
                ('description', models.TextField(max_length=1000, verbose_name='Descripción')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Códigos SGA',
                'verbose_name_plural': 'Código SGA',
            },
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ubicación/Asignaturas')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultad', to='reactivos.facultades', verbose_name='Facultad')),
            ],
            options={
                'verbose_name': 'Ubicación/Asignaturas',
                'verbose_name_plural': 'Ubicaciones/Asignaturas',
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Unidad')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.DeleteModel(
            name='Reactivo',
        ),
        migrations.DeleteModel(
            name='Unity',
        ),
        migrations.AddField(
            model_name='salidas',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='reactivos.ubicaciones', verbose_name='Ubicación'),
        ),
        migrations.AddField(
            model_name='salidas',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='reactivos.responsables', verbose_name='Responsable'),
        ),
        migrations.AddField(
            model_name='salidas',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_react', to='reactivos.reactivos', verbose_name='Nombre Reactivo'),
        ),
        migrations.AddField(
            model_name='salidas',
            name='trademark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_trademark', to='reactivos.marcas', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='reactivos',
            name='SGA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resp', to='reactivos.sga', verbose_name='Clasificación SGA'),
        ),
        migrations.AddField(
            model_name='reactivos',
            name='respel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respel', to='reactivos.respelc', verbose_name='Clasificación Respel'),
        ),
        migrations.AddField(
            model_name='reactivos',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='reactivos.estados', verbose_name='Presentación'),
        ),
        migrations.AddField(
            model_name='reactivos',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactive', to='reactivos.unidades', verbose_name='Unidad'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laboratorio', to='reactivos.laboratorios', verbose_name='Laboratorio'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactivos.reactivos', verbose_name='Nombre del reactivo'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='trademark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactivos.marcas', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidad', to='reactivos.unidades', verbose_name='Unidades'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='wlocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wloc', to='reactivos.almacenamiento', verbose_name='Ubicación en Almacén'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='reactivos.laboratorios', verbose_name='Laboratorio'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ubicacion', to='reactivos.ubicaciones', verbose_name='Ubicación'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to='reactivos.responsables', verbose_name='Responsable'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_reactivo', to='reactivos.reactivos', verbose_name='Nombre Reactivo'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='trademark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_marca', to='reactivos.marcas', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='entradas',
            name='wlocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wlocation', to='reactivos.almacenamiento', verbose_name='Ubicación en Almacén'),
        ),
        migrations.AddField(
            model_name='almacenamiento',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labrel', to='reactivos.laboratorios', verbose_name='Laboratorio'),
        ),
    ]
