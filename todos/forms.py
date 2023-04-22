from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title'}),
            'description': forms.Textarea(attrs={'class': 'form-description'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-completed'}),
            }