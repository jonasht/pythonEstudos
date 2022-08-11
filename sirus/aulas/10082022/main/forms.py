from django import forms
from .models import Usuario



class formUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        