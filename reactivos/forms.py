from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm
from reactivos.models import User, Rol, Laboratorios,Solicitudes, ConfiguracionSistema
import re


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modifica el widget del campo username para que sea visible en el admin
        self.fields['username'].widget = forms.EmailInput(attrs={'autocomplete': 'email'})

class ReCaptchaForm(forms.Form):
    # Campo de reCAPTCHA
    captcha = ReCaptchaField()

class CustomPasswordResetForm(PasswordResetForm):
    # Realiza aquí las modificaciones que desees en el formulario
    # Agrega el campo de reCAPTCHA
    captcha = ReCaptchaField()
    pass


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
    return nombre

class FormularioUsuario(forms.ModelForm):
      
    password1 = forms.CharField(label='Contraseña: ', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la contraseña',
            'id': 'password1',
            'required': 'required',
            'title':'La contraseña debe tener mínimo 8 caracteres,  al menos una mayúscula, un número, y un caracter especial',
            'pattern': '^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        }
    ))

    password2 = forms.CharField(label='Confirmación de contraseña: ', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba nuevamente la contraseña',
            'id': 'password2',
            'required': 'required',
            'title':'La contraseñas debe tener mínimo 8 caracteres,  al menos una mayúscula, un número, y un caracter especial',
            'pattern': '^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
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
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        # Validación de que las contraseñas sean iguales
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password2

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
                    'class': 'form-control',
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
        label="Introduzca el tiempo para depuración de solicitudes",
    )

    tiempo_eventos = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días que durará las solicitudes tramitadas',
                                        'placeholder':'Número de días de solicitudes tramitadas',}),
        required=True,
        label="Introduzca el tiempo para depuración de eventos",
        
    )

    correo_administrador = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'title':'Introduzca el correo para recepción de solicitudes',
                                       'placeholder':'Correo para recepción de solicitudes',}),
        required=True,
        label="Introduzca el correo de administrador para solicitudes",
    )
    tiempo_vencimiento_reactivos=forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días previos al vencimiento de reactivos',
                                        'placeholder':'Número de días antes del vencimiento de reactivos',}),
        required=True,
        label="Introduzca el tiempo previo de vencimeinto de reactivos para alertas",
        
    )
    intervalo_tiempo=forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'title':'Introduzca el número de días para revisión de vencimiento de reactivos',
                                        'placeholder':'Intervalo de días para revisión de vencimientos',}),
        required=True,
        label="Periodicidad para la  revisión de fecha de vencimientos (días)",
        
    )
    fecha_incio= forms.DateTimeField(
        widget=forms.DateTimeInput (attrs={'class': 'form-control',
                                        'title':'Introduzca la fecha de inicio para revisión de los vencimientos',
                                        'placeholder':'Fecha de incio',}),
                                        required=True,
                                        label="Fecha de inicio",
    )
    
    programacion_activa=forms.BooleanField(
        widget=forms.NullBooleanSelect (attrs={'class': 'form-control',
                                        'title':'Activar / Desactivar Programación',
                                        }),
                                        required=False,
                                        label="Activar o desactivar programación de revisión de fechas de vencimientos",
                                        
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

    class Meta:
        model = ConfiguracionSistema
        fields = ['tiempo_solicitudes', 'tiempo_eventos', 'correo_administrador','tiempo_vencimiento_reactivos','intervalo_tiempo','fecha_incio','programacion_activa','manual']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['correo_administrador'] = estandarizar_nombre(cleaned_data['correo_administrador'])
        