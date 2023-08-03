#Este archivo configuera los modelos para realizar la gestión de la base de datos, tanto en el motor como en el admin
from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser,User,Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

class Rol(models.Model):
    name=models.CharField('Rol', max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Rol'
    def __str__(self):
        return self.name
    def save(self, *args,**kwargs):
        permisos_defecto=['add','change','delete','view']
        if not self.id:
            nuevo_grupo,creado=Group.objects.get_or_create(name=f'{self.name}')
            for permiso_temporal in permisos_defecto:
                permiso,created = Permission.objects.update_or_create(
                    name = f'Can {permiso_temporal} {self.name}',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temporal}_{self.name}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args,**kwargs)
        else:
            rol_antiguo = Rol.objects.filter (id=self.id).values('name').first()
            if rol_antiguo['name'] == self.name:
                super().save(*args,**kwargs)
            else:
                Group.objects.filter(name=rol_antiguo['name']).update(name = f'{self.name}')
                print(f'Actualicé el grupo por {self.name}')
                for permiso_temp in permisos_defecto:
                    print(f"Ahora voy a actualizar el permiso {permiso_temp}_{rol_antiguo['name']}")
                    Permission.objects.filter(codename= f"{permiso_temp}_{rol_antiguo['name']}").update(
                        codename=f'{permiso_temp}_{self.name}',
                        name=f'Can {permiso_temp} {self.name}'
                    )
                    super().save(*args,**kwargs)



class User(AbstractUser): 
    email = models.EmailField('Correo Electrónico', unique=True)
    lab = models.ForeignKey('reactivos.Laboratorios', on_delete=models.CASCADE, related_name='lab_users', verbose_name='laboratorio', null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización',)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def save(self, *args,**kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            
            if self.rol is not None:
                grupo = Group.objects.filter(name=self.rol.name).first()
                if grupo:
                    self.groups.add(grupo)
                super().save(*args,**kwargs)
        else:
            if self.rol is not None:
                grupo_antiguo = User.objects.filter(id=self.id).values('rol__name').first()
                if grupo_antiguo['rol__name'] == self.rol.name:
                    super().save(*args,**kwargs)
                else:
                    grupo_anterior = Group.objects.filter(name=grupo_antiguo['rol__name']).first()
                    if grupo_anterior:
                        self.groups.remove(grupo_anterior)
                    nuevo_grupo=Group.objects.filter(name=self.rol.name).first()
                    if nuevo_grupo:
                        self.groups.add(nuevo_grupo)
                    super().save(*args,**kwargs)      



# Modelo para tabla Unidades en base de datos Reactivos
class Unidades(models.Model):
    name = models.CharField(max_length=20, verbose_name="Unidad")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por', related_name='updateby_units',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Unidades'
        verbose_name = 'Unidad'

# Modelo para tabla Marcas en base de datos Reactivos
class Marcas(models.Model):
    name = models.CharField(max_length=30, verbose_name="Marca")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Registro')
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_trademarks',)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Marcas'
        verbose_name = 'Marca'

    
# Modelo para tabla Estados en base de datos Reactivos
class Estados(models.Model):
    name = models.CharField(max_length=30, verbose_name="Estado")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_states',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Estados'
        verbose_name = 'Estado'

# Modelo para tabla Destinos en base de datos Reactivos
class Destinos(models.Model):
    name = models.CharField(max_length=30, verbose_name="Destino")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_destinations',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Destinos'
        verbose_name = 'Destino'

# Modelo para tabla Laboratorios en base de datos Reactivos
class Laboratorios(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre Laboratorio")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_labs', verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_labs',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Laboratorios'
        verbose_name = 'Laboratorio'

# Modelo para tabla Responsables en base de datos Reactivos
class Responsables(models.Model):
    cc=models.IntegerField(verbose_name="Cédula")
    name = models.CharField(max_length=255, verbose_name="Nombre Responsable")
    mail = models.EmailField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_manager',)     

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Responsables'
        verbose_name = 'Responsable'

# Modelo para tabla Facultades en base de datos Reactivos
class Facultades(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre Facultad")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por', related_name='updateby_school',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Facultades'
        verbose_name = 'Facultad'


# Modelo para tabla RespelC en base de datos Reactivos
class RespelC(models.Model):
    name = models.CharField(max_length=100, verbose_name="Clasificación Respel")
    description=models.TextField(max_length=1000, verbose_name="Descripción")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_respel',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Clasificación Respel'
        verbose_name = 'Clasificación Respel'

# Modelo para tabla SGA en base de datos Reactivos
class SGA(models.Model):
    name = models.CharField(max_length=100, verbose_name="Codificiación SGA")
    description=models.TextField(max_length=1000, verbose_name="Descripción")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_sga',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Codificiación SGA'
        verbose_name = 'Codificiación SGA'

# Modelo para tabla Ubicaciones en base de datos Reactivos
class Ubicaciones(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Ubicación/Asignaturas")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    facultad = models.ForeignKey(
        Facultades, on_delete=models.CASCADE, related_name='facultad', verbose_name='Facultad')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por', related_name='updateby_location',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ubicaciones/Asignaturas'
        verbose_name = 'Ubicación/Asignaturas'

# Modelo para tabla Almacenamiento (Ubicaciones en almacén) en base de datos Reactivos
class Almacenamiento(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    name = models.CharField(
        max_length=100, verbose_name="Ubicación/Asignaturas")
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='labrel', verbose_name='Laboratorio')    
    description=models.TextField(max_length=1000, verbose_name="Descripción")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por', related_name='updateby_storage',)

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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_reactive',)

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

    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro',)
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    name = models.ForeignKey(Reactivos, on_delete=models.CASCADE,
                             related_name='name_reactivo', verbose_name='Nombre Reactivo')
    trademark = models.ForeignKey(
        Marcas, on_delete=models.CASCADE, related_name='name_marca', verbose_name='Marca')
    reference = models.CharField(max_length=255, verbose_name='Referencia')
    weight = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Cantidad de entrada")
    order = models.CharField(max_length=255,  verbose_name='Orden No.')
    manager = models.ForeignKey(Responsables, on_delete=models.CASCADE,
                                related_name='responsable', verbose_name='Responsable')
    observations = models.TextField(
        max_length=1000, verbose_name='Observaciones')
    location = models.ForeignKey(
        Ubicaciones, on_delete=models.CASCADE, related_name='Ubicacion', verbose_name='Asignatura/Ubicación')
    price=models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Valor")
    
    nproject=models.CharField(max_length=15, verbose_name='Número de proyecto')
    destination=models.ForeignKey(Destinos, on_delete=models.CASCADE, verbose_name='Destino')
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='labs', verbose_name='Laboratorio')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_in',)
    
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
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    name = models.ForeignKey(Reactivos, on_delete=models.CASCADE,
                             related_name='name_react', verbose_name='Nombre Reactivo')
    trademark = models.ForeignKey(
        Marcas, on_delete=models.CASCADE, related_name='name_trademark', verbose_name='Marca')
    reference = models.CharField(max_length=255, verbose_name='Referencia')
    weight = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Cantidad de salida")
    destination = models.ForeignKey(
        Destinos, on_delete=models.CASCADE, related_name='destination', verbose_name='Destino')
    manager = models.ForeignKey(Responsables, on_delete=models.CASCADE,
                                related_name='manager', verbose_name='Responsable')
    observations = models.TextField(
        max_length=1000, verbose_name='Observaciones')
    location = models.ForeignKey(
        Ubicaciones, on_delete=models.CASCADE, related_name='location', verbose_name='Ubicación')
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='lab', verbose_name='Laboratorio')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por', related_name='updateby_out',)
    
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
    weight = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Cantidad en inventario")
    reference = models.CharField(max_length=20, verbose_name="Referencia")
    lab=models.ForeignKey(Laboratorios, on_delete=models.CASCADE, related_name='laboratorio', verbose_name='Laboratorio')
    wlocation=models.ForeignKey(Almacenamiento, on_delete=models.CASCADE, related_name='wloc', verbose_name='Ubicación en Almacén')
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Registro')
    ultima_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Última Actualización')
    edate=models.DateField(verbose_name="Fecha de vencimiento")
    minstock = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, default=0, help_text="Ingrese el stock mínimo (puede ser nulo).", verbose_name="Stock mínimo")
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Actualizado por',related_name='updateby_inventory',)

    class Meta:
        verbose_name_plural = "Inventarios"

    def __str__(self):
        return f"{self.reactivo.nombre} ({self.marca.nombre}): {self.cantidad}"

#Modelo Ficticio para la página de incio pueda ser incluido en la administración de Django
class PaginaInicio(models.Model):
    class Meta:
        managed = False  # Indica que no se debe crear una tabla en la base de datos

    def __str__(self):
        return "Página de inicio"


@receiver(pre_save, sender=Unidades)
@receiver(pre_save, sender=Marcas)
@receiver(pre_save, sender=Estados)
@receiver(pre_save, sender=Destinos)
@receiver(pre_save, sender=Laboratorios)
@receiver(pre_save, sender=Responsables)
@receiver(pre_save, sender=Facultades)
@receiver(pre_save, sender=RespelC)
@receiver(pre_save, sender=SGA)
@receiver(pre_save, sender=Ubicaciones)
@receiver(pre_save, sender=Almacenamiento)
@receiver(pre_save, sender=Reactivos)
@receiver(pre_save, sender=Entradas)
@receiver(pre_save, sender=Salidas)
@receiver(pre_save, sender=Inventarios)
def set_last_updated_by(sender, instance, **kwargs):
        instance.last_updated_by = instance.user  # Asignamos el usuario actual antes de guardar