from django.db import models


class Unidades(models.Model):
    name=models.CharField(max_length=20, verbose_name="Unidad")

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Unidades'
        verbose_name='Unidad'


class Reactivos(models.Model):
    color=models.PositiveIntegerField( verbose_name="Color CGA")
    number=models.CharField(max_length=5, verbose_name="Número")
    subnumber=models.CharField(max_length=3, verbose_name="Sub-número")
    code=models.CharField(max_length=255, verbose_name="Código")
    name=models.CharField(max_length=255, verbose_name="Nombre")
    unit=models.ForeignKey(Unidades, on_delete=models.CASCADE, related_name='reactive', verbose_name="Unidad")
    cas=models.CharField(max_length=20, verbose_name="Código CAS")
    is_liquid=models.CharField(max_length=3, verbose_name="Es líquido")
    is_active=models.BooleanField(default=True)
    wlocation=models.CharField(max_length=255, verbose_name="Ubicación Almacén")

    def __str__ (self):
        return self.name
    
    @property
    def unity_name (self):
        return self.unity.name
    
    class Meta:
        verbose_name_plural='Reactivos'
        verbose_name='Reactivo'

class Marcas(models.Model):
    name=models.CharField(max_length=30, verbose_name="Marca")

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Marcas'
        verbose_name='Marca'

class Destinos(models.Model):
    name=models.CharField(max_length=30, verbose_name="Destino")

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Destinos'
        verbose_name='Destino'


class Asignaturas(models.Model):
    name=models.CharField(max_length=30, verbose_name="Asignatura")

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Asignaturas'
        verbose_name='Asignatura'




class Responsables(models.Model):
    name=models.CharField(max_length=255, verbose_name="Nombre Responsable")
    mail=models.EmailField(max_length=255, verbose_name="Email")
    phone=models.BigIntegerField(verbose_name="Teléfono")
    is_active=models.BooleanField(default=True)

    def __str__ (self):
        return self.name
    
   
    
    class Meta:
        verbose_name_plural='Responsables'
        verbose_name='Responsable'


class Salidas(models.Model):
    date=models.DateTimeField(verbose_name='Fecha')
    name=models.ForeignKey(Reactivos, on_delete=models.CASCADE, related_name='name_react', verbose_name='Nombre Reactivo')
    trademark=models.ForeignKey(Marcas, on_delete=models.CASCADE, related_name='name_trademark', verbose_name='Marca')
    reference=models.CharField(max_length=255, verbose_name='Referencia')
    weight=models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Peso Reactivo')
    is_liquid=models.BooleanField(default=False, verbose_name='Es líquido')
    destination=models.ForeignKey(Destinos, on_delete=models.CASCADE, related_name='destination', verbose_name='Destino')
    schoolsubject=models.ForeignKey(Asignaturas, on_delete=models.CASCADE, related_name='ssubject', verbose_name='Asignatura')
    manager=models.ForeignKey(Responsables, on_delete=models.CASCADE, related_name='manager', verbose_name='Responsable')
    observations=models.TextField(max_length=1000, verbose_name='Observaciones')
    out_reagent=models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Total Salida')

    def __str__ (self):
        return self.name
    
    @property
    def unity_name (self):
        return self.unity.name
    
    class Meta:
        verbose_name_plural='Salidas'
        verbose_name='Salida'
