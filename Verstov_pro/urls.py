from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('url_shortener.urls')),
    path('', include('private_notes.urls')),
    path('audio_test/', include('audio_test.urls')),

    path(r'favicon.ico', RedirectView.as_view(url=f'{settings.STATIC_URL}/favicon.ico', permanent=True)),
]

# make media files available
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
