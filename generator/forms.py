from django import forms


class cargarArchivoForm(forms.Form):
    archivo = forms.FileField(
        label="Seleccione un archivo", widget=forms.FileInput(attrs={"class": "form-control mb-2"})
    )
    cantidadPreguntas = forms.IntegerField(
        label="Cantidad de preguntas",
        widget=forms.NumberInput(attrs={"class": "form-control mb-2", "min": "1", "max": "10"}),
    )
