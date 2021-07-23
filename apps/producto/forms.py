from django import forms
from .models import Producto
def agregarFormControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form-control'

class FormularioProducto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioProducto, self).__init__(*args, **kwargs)
        agregarFormControl(self.visible_fields())
        
    class Meta:
        model = Producto
        fields =  '__all__'
