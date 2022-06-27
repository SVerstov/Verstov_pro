""" Signals here delete unnecessary files in media/audio_test """

import os
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from .models import AudioComposition
from django.conf import settings


@receiver(pre_delete, sender=AudioComposition)
def delete_media_files(sender, instance, **kwargs):
    instance.uncompressed_audio.delete(False)
    instance.mp3_high.delete(False)
    instance.mp3_lowest.delete(False)
    instance.photo.delete(False)


@receiver(post_delete, sender=AudioComposition)
def delete_empty_folders_receiver(sender, **kwargs):
    def delete_empty_folders(path):
        for root, dirs, files in os.walk(path):
            for d in dirs:
                dir = os.path.join(root, d)
                if not os.listdir(dir):
                    os.rmdir(dir)
                delete_empty_folders(dir)

    delete_empty_folders(os.path.join(settings.MEDIA_ROOT, 'audio_test'))
