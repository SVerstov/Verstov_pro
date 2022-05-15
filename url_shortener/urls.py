from django.urls import path
from .views import *

urlpatterns = (
    path('shortener/', shortener, name='shortener'),
    path('<slug:short_id>', redirect_to_main_url),

)


