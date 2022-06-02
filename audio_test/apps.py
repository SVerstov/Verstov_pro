from django.apps import AppConfig


class AudioTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'audio_test'
    verbose_name = 'Аудио тест'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals

