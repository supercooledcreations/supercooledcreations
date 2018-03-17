# Import
# Django
from django.contrib import admin

# App
from .models import BaseMetric, DetailMetric


# Admin
admin.site.register(BaseMetric)
admin.site.register(DetailMetric)


