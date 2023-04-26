from django.db import models


class Unidades(models.Model):
    name=models.CharField(max_length=20)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Unidades'
        verbose_name='Unidad'


class Reactivos(models.Model):
    color=models.PositiveIntegerField()
    number=models.CharField(max_length=5)
    subnumber=models.PositiveIntegerField(null=True, blank=True)
    code=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    unit=models.ForeignKey(Unidades, on_delete=models.CASCADE, related_name='reactive')
    density=models.DecimalField(max_digits=10, decimal_places=4)
    is_active=models.BooleanField(default=True)

    def __str__ (self):
        return self.name
    
    @property
    def unity_name (self):
        return self.unity.name
    
    class Meta:
        verbose_name_plural='Reactivos'
        verbose_name='Reactivo'

class Marcas(models.Model):
    name=models.CharField(max_length=30)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Marcas'
        verbose_name='Marca'

class Destinos(models.Model):
    name=models.CharField(max_length=30)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Destinos'
        verbose_name='Destino'


class Asignaturas(models.Model):
    name=models.CharField(max_length=30)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Asignaturas'
        verbose_name='Asignatura'




class Responsables(models.Model):
    name=models.CharField(max_length=255)
    mail=models.EmailField(max_length=255)
    phone=models.BigIntegerField()
    is_active=models.BooleanField(default=True)

    def __str__ (self):
        return self.name
    
    # @property
    # def unity_name (self):
    #     return self.unity.name
    
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
