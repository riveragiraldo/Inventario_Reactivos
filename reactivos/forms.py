from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm
from reactivos.models import User, Rol, Laboratorios,Solicitudes, ConfiguracionSistema, SolicitudesExternas
import re
from captcha.fields import CaptchaField, CaptchaTextInput


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modifica el widget del campo username para que sea visible en el admin
        self.fields['username'].widget = forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'})

# Actualiza para añadir recaptcha al formulario de restablecimiento de la contraseña
class CustomPasswordResetForm(PasswordResetForm):
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class':'form-control', 'id':'recaptcha'}),
                           label='Captcha (Solucione la operación):',)


#--------------------------------------Formulario Crear Usuario--------------------------------------
def estandarizar_nombre(nombre):
    nombre = nombre.upper()
    nombre = re.sub('[áÁ]', 'A', nombre)
    nombre = re.sub('[éÉ]', 'E', nombre)
    nombre = re.sub('[íÍ]', 'I', nombre)
    nombre = re.sub('[óÓ]', 'O', nombre)
    nombre = re.sub('[úÚ]', 'U', nombre)
    nombre = re.sub('[ñÑ]', 'N', nombre)
    nombre = re.sub('[^A-Za-z0-9@ .,()_-]', '', nombre)
    nombre = nombre.strip()  # Eliminar espacios al principio y al final
    return nombre

class FormularioUsuario(forms.ModelForm):
      
    password1 = forms.CharField(label='Contraseña: ', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la contraseña',
            'id': 'password1',
            'required': 'required',
            'title':'La contraseña debe tener mínimo 8 caracteres,  al menos una mayúscula, un número, y un caracter especial',
            'pattern': '^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            'autocomplete':'off',

        }
    ))

    password2 = forms.CharField(label='Confirmación de contraseña: ', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba nuevamente la contraseña',
            'id': 'password2',
            'required': 'required',
            'title':'La contraseñas debe tener mínimo 8 caracteres,  al menos una mayúscula, un número, y un caracter especial',
            'pattern': '^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            'autocomplete':'new-password',
        }
    ))
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label='Rol', required=True,
                                 widget=forms.Select(
                                     attrs={
                                         'class': 'form-control',
                                         'required':'required'
                                         }))
    
    id_number = forms.IntegerField(label='Cédula', required=True,
                                   widget=forms.NumberInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Número de identificación',
                                           'pattern':'^(?:[1-9]\d{6,10}|9999999999)$',
                                           'title':'Ingrese un número de cédula entre 1000000 y 9999999999 (sin puntos ni comas)',
                                           'required':'required',
                                           'id':'id_number'

                                       }))
    
    phone_number = forms.IntegerField(label='Número Telefónico', required=True,
                                      widget=forms.NumberInput(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Número Telefónico',
                                              'pattern':'[0-9]{10,13}',
                                              'title':'Ingrese su número telefónico (solo números enteros positivos de 10 a 13 dígitos)',
                                              'required':'required'
                                              }))
    
    lab = forms.ModelChoiceField(queryset=Laboratorios.objects.all(), label='Laboratorio', required=True,
                                 widget=forms.Select(
                                     attrs={
                                         'class': 'form-control',
                                         'required':'required'
                                         }))
    acceptDataProcessing = forms.BooleanField(required=True,
                                              widget=forms.CheckboxInput(attrs={
                                                  'required':'required',
                                                  'id':'acceptDataProcessing',
                                                  'name':'acceptDataProcessing',
                                                  'checked':'checked',
                                                
                                              }))
    
    email = forms.EmailField(label='Correo Electrónico', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico',
            'id': 'email',
            'required':'required',
            'pattern':'^[a-zA-Z0-9.-_]+@[a-zA-Z]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]+)?$',
            'title':'Ingrese una dirección de correo electrónico válida (max 40 caracteres)',
            'maxlength':'100'
            }))
    
    username=forms.CharField(label='Nombre de usuario', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el nombre de usuario',
            'id': 'username',
            'required':'required',
            'pattern':'^(?:[a-zA-Zá-úÁ-Ú]+\s){0,1}[a-zA-Zá-úÁ-Ú]+$',
            'title':'Ingrese solo una palabras sin números ni caracteres especiales',
            }))

    class Meta:
        model = User  
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba los nombres',
                    'id': 'first_name',
                    'required':'required',
                    'pattern':'^(?:[a-zA-Zá-úÁ-Ú]+\s){0,1}[a-zA-Zá-úÁ-Ú]+$',
                    'title':'Ingrese máximos dos palabras sin números ni caracteres especiales',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba sus apellidos',
                    'id': 'last_name',
                    'required':'required',
                    'pattern':'^(?:[a-zA-Zá-úÁ-Ú]+\s){0,1}[a-zA-Zá-úÁ-Ú]+$',
                    'title':'Ingrese máximos dos palabras sin números ni caracteres especiales',
                }
            ),
            }
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['first_name'] = estandarizar_nombre(cleaned_data['first_name'])
        cleaned_data['last_name'] = estandarizar_nombre(cleaned_data['last_name'])
        return cleaned_data
    
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
        
    #     # Validación de que las contraseñas sean iguales
    #     if password1 != password2:
    #         raise forms.ValidationError('Las contraseñas no coinciden')
        
    #     return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))  # Usar 'pasword1' en lugar de 'password1'
        if commit:
            user.save()
        return user
# Formulario para el registro de solicitudes    
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ('tipo_solicitud', 'name', 'mensaje', 'archivos_adjuntos')
        widgets = {
            'tipo_solicitud': forms.Select(
                attrs={
                    'class': 'form-control',  
                    'id': 'tipo_solicitud',
                    'required': 'required',
                    'title': 'Seleccione el tipo de solicitud',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Escriba el nuevo tipo de solicitud',
                    'class': 'form-control',
                    'id': 'name',
                    'title': 'Escriba el tipo de solicitud máximo 100 caracteres',
                    'pattern': '.{1,100}',  # Agregar el patrón para 1 a 100 caracteres
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'placeholder': 'Escriba el detalle de su solicitud',
                    'class': 'form-control',
                    'id': 'mensaje',
                    'required': 'required',
                    'title': 'Escriba el detalle de su solicitud máximo 1000 caracteres',
                    'rows': '5',  # Máximo de 5 filas
                    'maxlength': '1000',  # Máximo de 1000 caracteres
                    'pattern': '.{1,1000}',  # Patrón para 1 a 1000 caracteres
                }
            ),
            'archivos_adjuntos': forms.FileInput(
                attrs={
                    'class':'custom-file-input',
                    'id': 'archivos_adjuntos',
                    'title': 'Adjunte archivos de tamaño maximo 5 MB',
                    'rows': '5',  # Máximo de 5 filas
                    'maxlength': '1000',  # Máximo de 1000 caracteres
                    'pattern': '.{1,1000}',  # Patrón para 1 a 1000 caracteres
                }
            )
        }
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['mensaje'] = estandarizar_nombre(cleaned_data['mensaje'])
        if cleaned_data['name']:
            cleaned_data['name'] = estandarizar_nombre(cleaned_data['name'])

# Formualrio para configuración del sistema

class ConfiguracionSistemaForm(forms.ModelForm):
    tiempo_solicitudes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días que durará los eventos en el sistema',
                                        'placeholder':'Número de días de los eventos en el sistema',}),
        required=True,
        label="*Introduzca el tiempo para depuración de solicitudes",
    )

    tiempo_eventos = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días que durará las solicitudes tramitadas',
                                        'placeholder':'Número de días de solicitudes tramitadas',}),
        required=True,
        label="*Introduzca el tiempo para depuración de eventos",
        
    )

    correo_administrador = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'title':'Introduzca el correo para recepción de solicitudes',
                                       'placeholder':'Correo para recepción de solicitudes',}),
        required=True,
        label="*Introduzca el correo de administrador para solicitudes",
    )
    tiempo_vencimiento_reactivos=forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días previos al vencimiento de reactivos',
                                        'placeholder':'Número de días antes del vencimiento de reactivos',}),
        required=True,
        label="*Introduzca el tiempo previo de vencimeinto de reactivos para alertas",
        
    )
    intervalo_tiempo=forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días para revisión de vencimiento de reactivos',
                                        'placeholder':'Intervalo de días para revisión de vencimientos',}),
        required=True,
        label="*Periodicidad para la  revisión de fecha de vencimientos (días)",
        
    )
    fecha_incio= forms.DateTimeField(
        widget=forms.DateTimeInput (attrs={'class': 'form-control',
                                        'title':'Introduzca la fecha de inicio para revisión de los vencimientos',
                                        'placeholder':'Fecha de incio',}),
                                        required=True,
                                        label="*Fecha de inicio",
    )
    
    programacion_activa=forms.BooleanField(
        widget=forms.NullBooleanSelect (attrs={'class': 'form-control',
                                        'title':'Activar / Desactivar Programación',
                                        }),
                                        required=False,
                                        label="*Activar o desactivar programación de revisión de fechas de vencimientos",
                                        
    )
    manual=forms.FileField(
        widget=forms.FileInput(attrs={'class':'form.control',
                                      'title':'Manual de usuario - Máximo 5 MB',
                                      'accept':'.pdf',
                                      'size':'5242880',
                                      }),
                                        required=False,
                                        label='Manual de usuario'
    )
    logo_institucional=forms.ImageField (
        widget=forms.FileInput (attrs={'class':'form.control',
                                      'title':'Imagen de logo insitucional',
                                      'accept':'image/*',
                                      'size':'5242880',
                                      }),
                                        required=False,
                                        label='Logo Institucional'
    )

    class Meta:
        model = ConfiguracionSistema
        fields = ['tiempo_solicitudes', 'tiempo_eventos', 'correo_administrador','tiempo_vencimiento_reactivos','intervalo_tiempo','fecha_incio','programacion_activa','manual','logo_institucional']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['correo_administrador'] = estandarizar_nombre(cleaned_data['correo_administrador'])

# # Fomrulario de envío de correo
# class CorreoForm(forms.Form):
#     DESTINO_CHOICES = [
#         ('TODOS', 'TODOS'),
#     ] + [(rol.id, rol.name) for rol in Rol.objects.all()] + [('USUARIO_ESPECIFICO', 'USUARIO ESPECÍFICO')]

#     LAB_CHOICES = [
#         ('TODOS', 'TODOS'),
#     ] + [(lab.id, lab.name) for lab in Laboratorios.objects.all()]

#     destino = forms.ChoiceField(
#         choices=DESTINO_CHOICES,
#         label='Destino',
#         widget=forms.Select(attrs={'class': 'form-control', 'required':'required','title':'Seleccione un destino',})
#     )
#     laboratorio = forms.ChoiceField(
#         choices=LAB_CHOICES,
#         label='Laboratorio',
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-control', 'title':'Seleccione un laboratorio',})
#     )
#     usuario = forms.EmailField(
#         label='Usuario',
#         required=False,
#         widget=forms.EmailInput(attrs={'class': 'form-control','title':'El correo electrónico debe cumplir con los formatos válidos de un correo electrónico','pattern':'^[a-zA-Z0-9.-_]+@[a-zA-Z]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]+)?$',})
#     )
#     asunto = forms.CharField(
#     max_length=100,  # Limitar a 100 caracteres
#     label='*Asunto',
#     widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'required': 'required',
#             'placeholder': 'Escribe el asunto del mensaje',
#             'title': 'Escribe el asunto con un máximo de 100 caracteres',
#             'pattern': '.{1,100}',
#             }
#             )
#             )

#     mensaje = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control','required':'required','rows':'3','maxlength': '1000','title':'Escribe el mensaje con un máximo de 1000 caracteres', 'placeholder':'Escribe aquí el mensaje, (máx 1000 caracteres)'}),
#         label='*Mensaje'
#     )
#     adjunto = forms.FileField(
#         label='Adjuntar Archivo',
#         required=False,
#         widget=forms.ClearableFileInput(attrs={'class': 'form.control','title':'Adjunte archivos de máximo 5 MB',})
#     )
        
#Personalización del Captcha
class CustomCaptchaField(CaptchaField):
    def __init__(self, *args, **kwargs):
        super(CustomCaptchaField, self).__init__(*args, **kwargs)
        self.label = '*Captcha (Soluciona la operación):'
# Solicitudes externas
class SolicitudesExternasForm(forms.ModelForm):
    # Captcha
    captcha = CustomCaptchaField()

    # Campo adicional para el token de acceso
    access_token = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'access_token'}), required=False)
    # Obtener los nombres de los laboratorios para usar en el campo 'lab'
    lab_choices = [(lab.id, lab.name) for lab in Laboratorios.objects.all()]

    # Validador para números de móvil en el rango especificado
    mobile_number_validator = RegexValidator(
        regex='^[3-9]\d{9}$',
        message='El número de móvil debe estar en el rango de 3000000000 a 3999999999.',
    )

    

    # Definir el formulario
    class Meta:
        model = SolicitudesExternas
        fields = ['name', 'subject', 'message', 'attach', 'lab', 'email', 'mobile_number', 'department', 'accept_politics']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'title': 'Nombres y apellidos que incluyan solo letras con máximo de 50 caracteres', 'autocomplete': 'off'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'title': 'El asunto de la solicitud debe tener un máximo de 100 caracteres', 'autocomplete': 'off'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'title': 'El texto que describe la solicitud debe tener un máximo de 1000 caracteres', 'autocomplete': 'off'}),
            'attach': forms.FileInput(attrs={'title': 'Adjuntar archivo (Opcional)', 'autocomplete': 'off'}),
            'lab': forms.Select(attrs={'class': 'form-control', 'title': 'Seleccione un laboratorio, este campo es obligatorio', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'title': 'Ingrese un correo electrónico válido de la Universidad Nacional de Colombia (XXX@unal.edu.co)', 'readonly': 'readonly', 'autocomplete': 'off'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control', 'title': 'Ingrese un número de móvil válido en el rango de 3000000000 a 3999999999', 'autocomplete': 'off'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'title': 'Ingrese el departamento correspondiente (máximo 100 caracteres)', 'autocomplete': 'off'}),
            'accept_politics': forms.CheckboxInput (attrs={'title': 'Debe aceptar la política de tratamiento de datos personales', 'unchecked': 'unchecked', 'required':'required'}),
        }
        labels = {
            'name': '*Nombres y Apellidos',
            'subject': '*Asunto',
            'message': '*Mensaje',
            'attach': 'Archivos Adjuntos',
            'lab': '*Laboratorio al que va dirigido la solicitud',
            'email': '*Correo Electrónico',
            'mobile_number': '*Número de Móvil',
            'department': '*Dependencia',
        }
        help_texts = {
            'name': 'Ingrese su nombre y apellidos (Máximo 50 caracteres, sin números ni caracteres especiales).',
            'subject': 'Ingrese el asunto de la solicitud a tramitar. (Máximo 100 caracteres)',
            'message': 'Ingrese el texto que describe la solicitud. (Máximo 1000 caracteres)',
            'attach': 'Adjunte un archivo si es necesario (máximo 5 Mb).',
            'lab': 'Seleccione el laboratorio relacionado con la solicitud.',
            'email': 'Ingrese un correo electrónico válido de la Universidad Nacional de Colombia (XXX@unal.edu.co)',
            'mobile_number': 'Ingrese un número de móvil válido en el rango de 3000000000 a 3999999999',
            'department': 'Ingrese el área a la que pertenece (máximo 100 caracteres)',
        }

    def clean(self):
        cleaned_data = super().clean()
        if 'email' in cleaned_data:
            cleaned_data['email'] = estandarizar_nombre(cleaned_data['email'])
        if 'name' in cleaned_data:
            cleaned_data['name'] = estandarizar_nombre(cleaned_data['name'])
        if 'subject' in cleaned_data:
            cleaned_data['subject'] = estandarizar_nombre(cleaned_data['subject'])
        if 'message' in cleaned_data:
            cleaned_data['message'] = estandarizar_nombre(cleaned_data['message'])
        if 'department' in cleaned_data:
            cleaned_data['department'] = estandarizar_nombre(cleaned_data['department'])

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@unal.edu.co'):
            raise forms.ValidationError('El correo electrónico debe tener el dominio @unal.edu.co.')
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        if not (3000000000 <= int(mobile_number) <= 3999999999):
            raise forms.ValidationError('El número de móvil debe estar entre 3000000000 y 3999999999.')
        return mobile_number
    
    def clean_attach(self):
        attach = self.cleaned_data.get('attach', False)
        if attach:
            # Limite de tamaño: 5 MB
            if attach.size > 5 * 1024 * 1024:
                raise ValidationError('El tamaño del archivo adjunto debe ser como máximo de 5 MB.')
        return attach