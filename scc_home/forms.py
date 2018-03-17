# Imports
# Django
from django import forms

# App
from .models import Bookmark


# Forms
class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        exclude = ['user']