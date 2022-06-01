from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponse

from .forms import AudioCompositionForm
from .models import AudioComposition
from tasks import convert_wav_to_mp3


class ShowAudioTest(ListView):
    'Audio test homepage'
    model = AudioComposition
    template_name = 'audio_test/show_audio_test.html'
    context_object_name = 'songs'

    def get_queryset(self):
        """Filer. Only songs with is_published flag will get into queryset"""
        return AudioComposition.objects.filter(is_published=True).exclude(mp3_128='')


def add_new_audio(request):
    if request.method == 'GET':
        # todo проверка логина
        form = AudioCompositionForm()
        context = {'form': form}
        return render(request, 'audio_test/add_audio.html', context)
    elif request.method == 'POST':
        form = AudioCompositionForm(request.POST, request.FILES)
        if form.is_valid():
            audio_db_object = form.save()
            # start new parallel process => convert wav to mp3
            convert_wav_to_mp3.delay(pk=audio_db_object.pk)

            messages.success(request, 'Аудио обрабатывается и скоро будет доступно!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка')
        context = {'form': form}
        return render(request, 'audio_test/add_audio.html', context)


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
