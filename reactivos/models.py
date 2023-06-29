#Este archivo configuera los modelos para realizar la gestión de la base de datos, tanto en el motor como en el admin
from django.db import models

# Modelo para tabla Unidades en base de datos Reactivos
class Unidades(models.Model):
    name = models.CharField(max_length=20, verbose_name="Unidad")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Unidades'
        verbose_name = 'Unidad'

# Modelo para tabla Marcas en base de datos Reactivos
class Marcas(models.Model):
    name = models.CharField(max_length=30, verbose_name="Marca")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Marcas'
        verbose_name = 'Marca'

# Modelo para tabla Estados en base de datos Reactivos
class Estados(models.Model):
    name = models.CharField(max_length=30, verbose_name="Estado")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Estados'
        verbose_name = 'Estado'

# Modelo para tabla Destinos en base de datos Reactivos
class Destinos(models.Model):
    name = models.CharField(max_length=30, verbose_name="Destino")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Destinos'
        verbose_name = 'Destino'

# Modelo para tabla Responsables en base de datos Reactivos
class Responsables(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre Responsable")
    mail = models.EmailField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    is_active = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Responsables'
        verbose_name = 'Responsable'

# Modelo para tabla Facultades en base de datos Reactivos
class Facultades(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre Facultad")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Facultades'
        verbose_name = 'Facultad'

# Modelo para tabla Laboratorios en base de datos Reactivos
class Laboratorios(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre Laboratorio")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Laboratorios'
        verbose_name = 'Laboratorio'

# Modelo para tabla RespelC en base de datos Reactivos
class RespelC(models.Model):
    name = models.CharField(max_length=100, verbose_name="Clasificación Respel")
    description=models.TextField(max_length=1000, verbose_name="Descripción")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Clasificación Respel'
        verbose_name = 'Clasificación Respel'

# Modelo para tabla SGA en base de datos Reactivos
class SGA(models.Model):
    name = models.CharField(max_length=100, verbose_name="Codificiación SGA")
    description=models.TextField(max_length=1000, verbose_name="Descripción")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Codificiación SGA'
        verbose_name = 'Codificiación SGA'

# Modelo para tabla Ubicaciones en base de datos Reactivos
class Ubicaciones(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Ubicación/Asignaturas")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    facultad = models.ForeignKey(
        Facultades, on_delete=models.CASCADE, related_name='facultad', verbose_name='Facultad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ubicaciones/Asignaturas'
        verbose_name = 'Ubicación/Asignaturas'

# Modelo para tabla Almacenamiento (Ubicaciones en almacén) en base de datos Reactivos
class Almacenamiento(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=100, verbose_name="Ubicación/Asignaturas")
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='labrel', verbose_name='Laboratorio')    
    description=models.TextField(max_length=1000, verbose_name="Descripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ubicación en Almacén'
        verbose_name = 'Ubicación en Almacén'

# Modelo para tabla Reactivos en base de datos Reactivos
class Reactivos(models.Model):
    color = models.PositiveIntegerField(verbose_name="Color CGA")
    number = models.CharField(max_length=5, verbose_name="Número")
    subnumber = models.CharField(max_length=3, verbose_name="Sub-número")
    code = models.CharField(max_length=255, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    unit = models.ForeignKey(Unidades, on_delete=models.CASCADE,
                             related_name='reactive', verbose_name="Unidad")
    cas = models.CharField(max_length=20, verbose_name="Código CAS")
    state = models.ForeignKey(Estados, on_delete=models.CASCADE,
                              related_name='state', verbose_name="Presentación")
    respel = models.ForeignKey(RespelC, on_delete=models.CASCADE,
                              related_name='respel', verbose_name="Clasificación Respel")
    sga = models.ForeignKey(SGA, on_delete=models.CASCADE,
                              related_name='resp', verbose_name="Clasificación SGA")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def unity_name(self):
        return self.unity.name

    class Meta:
        verbose_name_plural = 'Reactivos'
        verbose_name = 'Reactivo'

# Modelo para tabla Entradas en base de datos Reactivos
class Entradas(models.Model):

    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    name = models.ForeignKey(Reactivos, on_delete=models.CASCADE,
                             related_name='name_reactivo', verbose_name='Nombre Reactivo')
    trademark = models.ForeignKey(
        Marcas, on_delete=models.CASCADE, related_name='name_marca', verbose_name='Marca')
    reference = models.CharField(max_length=255, verbose_name='Referencia')
    weight = models.DecimalField(
        max_digits=10, decimal_places=4, verbose_name='Peso Reactivo')
    order = models.CharField(max_length=255,  verbose_name='Orden No.')
    manager = models.ForeignKey(Responsables, on_delete=models.CASCADE,
                                related_name='responsable', verbose_name='Responsable')
    observations = models.TextField(
        max_length=1000, verbose_name='Observaciones')
    location = models.ForeignKey(
        Ubicaciones, on_delete=models.CASCADE, related_name='Ubicacion', verbose_name='Ubicación')
    price=models.IntegerField(verbose_name="Valor")
    
    nproject=models.CharField(max_length=15, verbose_name='Número de proyecto')
    destination=models.ForeignKey(Destinos, on_delete=models.CASCADE, verbose_name='Destino')
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='labs', verbose_name='Laboratorio')
    
    def __str__(self):
        return self.name

    @property
    def unity_name(self):
        return self.unity.name

    class Meta:
        verbose_name_plural = 'Entradas'
        verbose_name = 'Entrada'


# Modelo para tabla Salidas en base de datos Reactivos
class Salidas(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    name = models.ForeignKey(Reactivos, on_delete=models.CASCADE,
                             related_name='name_react', verbose_name='Nombre Reactivo')
    trademark = models.ForeignKey(
        Marcas, on_delete=models.CASCADE, related_name='name_trademark', verbose_name='Marca')
    reference = models.CharField(max_length=255, verbose_name='Referencia')
    weight = models.DecimalField(
        max_digits=10, decimal_places=4, verbose_name='Peso Reactivo')
    destination = models.ForeignKey(
        Destinos, on_delete=models.CASCADE, related_name='destination', verbose_name='Destino')
    manager = models.ForeignKey(Responsables, on_delete=models.CASCADE,
                                related_name='manager', verbose_name='Responsable')
    observations = models.TextField(
        max_length=1000, verbose_name='Observaciones')
    location = models.ForeignKey(
        Ubicaciones, on_delete=models.CASCADE, related_name='location', verbose_name='Ubicación')
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='lab', verbose_name='Laboratorio')
    
    

    def __str__(self):
        return self.name

    @property
    def unity_name(self):
        return self.unity.name

    class Meta:
        verbose_name_plural = 'Salidas'
        verbose_name = 'Salida'

# Modelo para tabla Inventarios en base de datos Reactivos
class Inventarios(models.Model):
    name = models.ForeignKey('Reactivos', on_delete=models.CASCADE, verbose_name="Nombre del reactivo")
    trademark = models.ForeignKey('Marcas', on_delete=models.CASCADE, verbose_name="Marca")
    weight = models.DecimalField(
        max_digits=10, decimal_places=4, verbose_name='Inventario Actual')
    unit = models.ForeignKey(Unidades, on_delete=models.CASCADE,
                             related_name='unidad', verbose_name="Unidades")
    reference = models.CharField(max_length=20, verbose_name="Referencia")
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='laboratorio', verbose_name='Laboratorio')
    wlocation=models.ForeignKey(Almacenamiento, on_delete=models.CASCADE, related_name='wloc', verbose_name='Ubicación en Almacén')
    fecha_registro = models.DateTimeField(auto_now=True,verbose_name='Últma actualización')
    edate=models.DateField(verbose_name="Fecha de vencimiento")
    minstock = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
        help_text="Ingrese el stock mínimo (puede ser nulo)."
    )
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name_plural = "Inventarios"

    def __str__(self):
        return f"{self.reactivo.nombre} ({self.marca.nombre}): {self.cantidad}"
