from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


def agregarFormControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form-control'

class RegistroUsuario(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        agregarFormControl(self.visible_fields())
        

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')


class IniciarSesion(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        agregarFormControl(self.visible_fields())

    class Meta:
        fields = ('username','password')