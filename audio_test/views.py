from django.views.generic import ListView
from django.http import HttpResponse

from .models import AudioComposition


class ShowAudioTest(ListView):
    'Audio test homepage'
    model = AudioComposition
    template_name = 'audio_test/show_audio_test.html'
    context_object_name = 'songs'

    def get_queryset(self):
        """Filer. Only songs with is_published flag will get into queryset"""
        return AudioComposition.objects.filter(is_published=True).exclude(mp3_128='')


def collect_statistics(request):
    song = AudioComposition.objects.get(pk=int(request.headers['Song-Id']))
    answer = request.headers['Answer']

    match answer:
        case 'wav':
            song.click_wav += 1
        case '128':
            song.clicks_on_128 += 1
        case '320':
            song.clicks_on_320 += 1
    song.save()

    return HttpResponse('')
