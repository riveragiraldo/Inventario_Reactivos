from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm
from reactivos.models import User, Rol, Laboratorios
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
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    id_number = forms.IntegerField(label='Cédula', required=False,
                                   widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de identificación'}))
    
    phone_number = forms.IntegerField(label='Número Telefónico', required=False,
                                      widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número Telefónico'}))
    
    lab = forms.ModelChoiceField(queryset=Laboratorios.objects.all(), label='Laboratorio', required=False,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = User  # Usar el signo igual (=) en lugar de dos puntos (:)
        fields = ('email', 'username', 'first_name', 'last_name')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                    'id': 'email',
                    'required':'required',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba los nombres',
                    'id': 'first_name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba sus apellidos',
                    'id': 'last_name'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                    'id': 'username'
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
