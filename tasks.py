""" Tasks file """
import django

django.setup()
from Verstov_pro.celery import app
from services.audio_convert import convert_to_mp3_and_save


@app.task
def convert_wav_to_mp3(pk: int):
    convert_to_mp3_and_save(pk)
    return f'Конвертация аудио заверщена. Всё записано в БД, {pk=}'
