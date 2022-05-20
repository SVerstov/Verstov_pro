from django.shortcuts import render
from audio_test.models import AudioComposition
from django.http import HttpResponse


def test(request):
    song = AudioComposition.objects.get(title='test')

    context = {"song": song}
    return render(request, 'experiments/test.html', context)


def test_js_request(request):
    print('Запрос с JS:')
    print(request.headers)
    print(request.session)
    return HttpResponse('')
