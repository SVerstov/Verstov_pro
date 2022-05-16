import re
from django.db import models
from django.core.validators import FileExtensionValidator
from django.http import HttpResponse
from django.urls import reverse


def content_file_name(instance, filename):
    """ make a path for a content MEDIA_ROOT/author/title/filename """
    author = delete_special_symbols(instance.author)
    title = delete_special_symbols(instance.title)
    return '/'.join(['audio_test', author, title, filename])


def delete_special_symbols(string):
    """ delete symbols that cannot be in a filename """
    return re.sub(r'[^\w\s]', '', string.strip())


class AudioComposition(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    author = models.CharField('Автор', max_length=150)
    photo = models.ImageField('Обложка', upload_to=content_file_name, blank=True)
    uncompressed_audio = models.FileField('Несжатое аудио', upload_to=content_file_name, blank=False,
                                          validators=[FileExtensionValidator(['wav'],
                                                                             "Файлы с расширением “%(extension)s” не подходят. "
                                                                             "Пожалуйста загрузите файл с расширением : %(allowed_extensions)s.")])
    mp3_320 = models.FileField(upload_to=content_file_name, blank=True)
    mp3_128 = models.FileField(upload_to=content_file_name, blank=True)
    # collect attempts statistic
    clicks_on_128 = models.IntegerField(default=0)
    clicks_on_320 = models.IntegerField(default=0)
    click_wav = models.IntegerField(default=0)

    is_published = models.BooleanField('опубликовано', default=True)

    def __str__(self):
        return self.title

    # def form_valid(self, form):
    #     print(f'Form is valid. Title - {form.title}')
    #     return HttpResponse('All is ok')
    #     return super().form_valid(form)
    #
    # def get_absolute_url(self):
    #     return reverse('home')


class Statistic(models.Model):
    headphones_attempts = models.IntegerField(default=0)
    headphones_points = models.IntegerField(default=0)
    speakers_attempts = models.IntegerField(default=0)
    speakers_points = models.IntegerField(default=0)
