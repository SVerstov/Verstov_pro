"""Verstov_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home.views import home
from experiments.views import test, test_js_request
from private_notes.views import create_private_note, find_and_check_private_note, input_second_password
from audio_test.views import show_audio_test, add_new_audio

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('', include('url_shortener.urls')),
    # private notes urls
    path('private_notes/', create_private_note, name='private_notes'),
    path('private_notes/second_password/', input_second_password, name='second_password'),
    path('<str:short_id>/<slug:password>', find_and_check_private_note),
    # audio test urls
    path('audio_test/', show_audio_test, name='show_audio_test'),
    path('audio_test/add/', add_new_audio, name='add_audio'),
    # my tests and experiments
    path('test/', test, name='test'),
    path('test/request/', test_js_request, name='test_js_request'),
]

# make media files available
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
pass