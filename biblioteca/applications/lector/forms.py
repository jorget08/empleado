from django import forms

from applications.libro.models import Libro

from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro'
        )


class MultiplePrestamoForm(forms.ModelForm):

    libros = forms.ModelMultipleChoiceField(
        queryset=None, # Se puede definir el queryset aqui mismo o con la def __init__ de abajo
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )
     
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        # Aqui le estamos diciendo que en en los campos pondra la variable libros que creamos antes de la clase Meta 
        # y en esa variable libros en su parametro queryset pondremos todos los objetos Libro que tenemos
        self.fields['libros'].queryset = Libro.objects.all()
    