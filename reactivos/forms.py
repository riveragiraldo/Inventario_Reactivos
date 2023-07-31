from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm




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
   
