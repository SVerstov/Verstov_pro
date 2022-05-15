from django.shortcuts import render
from audio_test.models import AudioComposition

# Create your views here.
def home(request):
    return render(request, 'home/home.html')






