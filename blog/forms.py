from django import forms
from .models import Autor, Post
from django.contrib.admin.widgets import AdminDateWidget

class post_form (forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget = forms.Textarea)
    fpublicado = forms.DateField(label="Fecha de publicación")
    autor = forms.ModelChoiceField(Autor.objects.all(), label="Autor")
    
class post_form_model(forms.ModelForm):
    fpublicado = forms.DateField(label='Fecha de publicación',
                                     input_formats=['%d/%m/%y', '%y-%m-%d'],
                                     widget=forms.DateInput(attrs={
                                         'class': 'form-control',
                                         'placeholder' : 'dd/mm/yyyy',
                                         'type':'date'
                                     }))    
    class Meta:
        model = Post
        fields = ["titulo", "cuerpo", "autor"]
        
class post_form_Model_Artista(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'email', 'dni', 'bio']