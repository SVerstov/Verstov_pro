from django.urls import path
from .views import *

urlpatterns = (
    path('', ShowAudioTest.as_view(), name='show_audio_test'),
    path('request/', collect_statistics),
)