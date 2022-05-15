from django.shortcuts import render
from audio_test.models import AudioComposition
from django.http import HttpResponse


def test(request):
    mp3_file = AudioComposition.objects.get(title='test').mp3_320

    context = {"mp3_file": mp3_file.url}
    return render(request, 'experiments/test.html', context)


def test_js_request(request):
    print('Запрос с JS:')
    print(request.headers)
    print(request.session)
    return HttpResponse('')
