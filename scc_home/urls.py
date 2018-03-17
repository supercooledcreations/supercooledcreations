# Imports
# Django
from django.urls import path

# App
from .views import HomeView

# Urls
app_name = 'scc_home'
urlpatterns = [
    # Bookmarks
    path('', HomeView.as_view(), name='home'),
]
