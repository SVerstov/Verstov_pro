from django.contrib import admin
from .models import AudioComposition
from django.utils.safestring import mark_safe


class AudioTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_photo', 'clicks_on_128', 'clicks_on_320', 'click_wav','is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    exclude = ('mp3_320', 'mp3_128', 'clicks_on_128', 'clicks_on_320', 'click_wav')

    def get_photo(self, obj):
        """Show photo in admin panel"""
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='60'>")
        else:
            return 'Нет фото'

    def save_model(self, request, obj, form, change):
        """ After save starts converting audio.
        celery and redis must be on work!
        """
        from tasks import convert_wav_to_mp3
        from django.contrib import messages

        audio_db_object = form.save()
        convert_wav_to_mp3.delay(pk=audio_db_object.pk)
        messages.success(request, 'Аудио обрабатывается и скоро будет доступно!')




admin.site.register(AudioComposition, AudioTestAdmin)
