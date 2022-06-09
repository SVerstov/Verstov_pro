import json

from django.views.generic import ListView
from django.http import HttpResponse
from .models import AudioComposition


class ShowAudioTest(ListView):
    """Audio test homepage"""
    model = AudioComposition
    template_name = 'audio_test/show_audio_test.html'
    context_object_name = 'songs'

    def get_queryset(self):
        """Filer. Only songs with is_published flag will get into queryset"""
        return AudioComposition.objects.filter(is_published=True).exclude(mp3_lowest='')


def collect_statistics(request):
    song = AudioComposition.objects.get(pk=int(request.POST.get('Song-Id')))
    answer = request.POST.get('Answer')
    print(request.POST.get('Answer'))

    # print(answer2)
    match answer:
        case 'wav':
            song.click_wav += 1
        case 'mp3_low':
            song.clicks_low_mp3 += 1
        case 'mp3_high':
            song.clicks_high_mp3 += 1
    song.save()

    return HttpResponse('')
