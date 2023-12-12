from django import forms
from .models import Libro, Usuario

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'anio_publicacion']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'contrasena']
    