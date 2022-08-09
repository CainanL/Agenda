from django.db import models
from contatos.models import Contato
from django import forms

# Create your models here.
class FormContato(forms.ModelForm):
    class Meta:
        model = Contato  # esse formulário representa contato, o modelo de formulário será como contato
        exclude = ('mostrar',)  # campos que eu quero excluir, "isso é uma tupla"
