from django.urls import path
from .views import *

urlpatterns = (
    path('private_notes/', create_private_note, name='private_notes'),
    path('private_notes/second_password/', input_second_password, name='second_password'),
    path('<str:short_id>/<slug:password>', find_and_check_private_note),
)
