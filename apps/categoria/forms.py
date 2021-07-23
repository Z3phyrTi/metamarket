from django import forms
from .models import Categoria
def agregarFormControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form-control'


class FormularioCategoria(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioCategoria, self).__init__(*args, **kwargs)
        agregarFormControl(self.visible_fields())

    class Meta:
        model = Categoria
        fields = '__all__'