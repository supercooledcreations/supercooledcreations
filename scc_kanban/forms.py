# Imports
# Django
from django import forms

# App
from .models import Task


# Forms
# Metric Forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
