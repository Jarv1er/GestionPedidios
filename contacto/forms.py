from django import forms


class FormContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, max_length=50)
    email = forms.CharField(label="Email", required=True, max_length=80)
    contenido = forms.CharField(widget=forms.Textarea)