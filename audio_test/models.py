import re
from django.db import models
from django.core.validators import FileExtensionValidator


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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField('Обложка', upload_to=content_file_name, blank=True)
    uncompressed_audio = models.FileField('Несжатое аудио', upload_to=content_file_name, blank=False,
                                          validators=[FileExtensionValidator(['wav'],
                                                                             "Файлы с расширением “%(extension)s” не подходят. "
                                                                             "Пожалуйста загрузите файл с расширением : %(allowed_extensions)s.")])

    mp3_high = models.FileField(upload_to=content_file_name, blank=True)
    mp3_lowest = models.FileField(upload_to=content_file_name, blank=True)
    quality = [(32, '32k'), (64, '64k'), (96, '96k'), (128, '128k')]
    mp3_lowest_quality = models.IntegerField('Наихудшее качество', blank=False, choices=quality, default=128)

    # collect attempts statistic
    clicks_low_mp3 = models.IntegerField(default=0)
    clicks_high_mp3 = models.IntegerField(default=0)
    click_wav = models.IntegerField(default=0)

    is_published = models.BooleanField('опубликовано', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аудио трек'
        verbose_name_plural = 'Аудио треки'
