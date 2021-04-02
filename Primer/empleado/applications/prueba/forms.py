from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        fields = ("titulo", "subtitulo", "cantidad")

        #Personalizamos el formulario para que tenga placeholder en el de titulo
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder' : "Ingrese texto aqui"
                }
            )
        }



    
    #Esta funcion es para cualquier regla que yo le quiera poner al usuario al momento de meter datos
    #por ejemplo aqui el dire que en cantidad tiene que se run dato mayor de 10 o sino no puede
    def clean_cantidad(self):
        #asi es como le digo a que campo se aplica la restriccion
        cantidad = self.cleaned_data['cantidad']

        #aqui la restriccion que quiero poner
        if cantidad < 10:
            raise forms.ValidationError('Ingresu un valor mayor de 10')

        return cantidad