from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

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
        return AudioComposition.objects.filter(is_published=True)



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


def convert_to_mp3_and_save():
    print('Im here')
    print(type())
    # mp.Process(target=convert_to_mp3_and_save, args=(audio_db_object,)).start()

    # mp.Process(target=do_something.main, args=['other', 'args']).start()

# class AddAudio(LoginRequiredMixin, CreateView):
#     form_class = AudioCompositionForm
#     template_name = 'audio_test/add_audio.html'
