# Imports
# Django
from django.urls import path

# App
from .views import (
    BaseMetricListView,
    BaseMetricDetailView,
)

# Urls
app_name = 'scc_kaizen'
urlpatterns = [
    # Metrics
    path('metrics/', BaseMetricListView.as_view(), name='metric_list'),
    path('metrics/<int:metric_pk>/', BaseMetricDetailView.as_view(), name='metric_detail'),
]
