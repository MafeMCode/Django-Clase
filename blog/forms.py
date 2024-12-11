from django import forms
from .models import Autor, Post
from django.contrib.admin.widgets import AdminDateWidget

class post_form (forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget = forms.Textarea)
    fpublicado = forms.DateField(label="Fecha de publicación")
    autor = forms.ModelChoiceField(Autor.objects.all(), label="Autor")
    
class post_form_model(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "cuerpo", "fpublicacion", "autor"]
        widgets = {
            'fpublicacion': AdminDateWidget(),
        }