from django.db import models


class Unidades(models.Model):
    name=models.CharField(max_length=20)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural='Unidades'


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

