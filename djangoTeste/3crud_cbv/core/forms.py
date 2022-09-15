from django import forms
from core.models import Cliente


class ClienteForms (forms.ModelForm):
    class Meta:
        model = Cliente
        frields = '__all__'
        
        
    