# Django Imports
from django.urls import path

# Project Imports
from . import views

app_name = 'scc_standard_user'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
