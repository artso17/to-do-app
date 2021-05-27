from django import forms
from django.forms import ModelForm
from .models import ListToDo


class TaskForm(forms.ModelForm):

    class Meta:
        model = ListToDo
        fields = '__all__'
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
        }
