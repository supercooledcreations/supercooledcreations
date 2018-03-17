# Django Imports
from django.contrib import admin

# Project Imports
from .models import StandardUser

# Admin Models
admin.site.register(StandardUser)
