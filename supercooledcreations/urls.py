# Import
# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

# Urls
urlpatterns = [
    path('', RedirectView.as_view(url='user/login/')),
    path('user/', include('scc_standard_user.urls', namespace='scc_standard_user')),
    path('home/', include('scc_home.urls', namespace='scc_home')),
    path('kaizen/', include('scc_kaizen.urls', namespace='scc_kaizen')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
