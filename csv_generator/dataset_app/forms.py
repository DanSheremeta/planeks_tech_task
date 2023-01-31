from django import forms
from . import models


class SchemaForm(forms.ModelForm):
    class Meta:
        model = models.Schema
        fields = ['title']
        labels = {
            'title': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
        }


class ColumnForm(forms.ModelForm):
    class Meta:
        model = models.Column
        fields = ['name', 'type', 'order']
        labels = {
            'name': '',
            'type': '',
            'order': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'Input', 'type': 'text'}),
            'type': forms.Select(attrs={'class': 'form-select', 'id': 'Select'}),
            'order': forms.TextInput(attrs={'class': 'form-control', 'id': 'Input1', 'type': 'text'}),
        }
