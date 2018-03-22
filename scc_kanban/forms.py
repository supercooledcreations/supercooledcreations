# Imports
# Django
from django import forms

# App
from .models import Task


# Forms
# Metric Forms
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']