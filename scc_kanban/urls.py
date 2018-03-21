# Imports
# Django
from django.urls import path

# App
from .views import (
    TaskListView
)

# Urls
app_name = 'scc_kanban'
urlpatterns = [
    # Tasks
    path('metrics/', TaskListView.as_view(), name='task_list'),
]
