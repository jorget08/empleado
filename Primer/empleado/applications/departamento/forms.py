from django import forms


#Regista un nuevo empleado y un departamento
class NewDptoYPersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    apellidos = forms.CharField(max_length=50, required=False)
    departamento = forms.CharField(max_length=50, required=False)
    short_name = forms.CharField(max_length=20, required=False)
