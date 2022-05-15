from django import forms

from .models import AudioComposition


class AudioCompositionForm(forms.ModelForm):
    """ describe fields with need to add new audio """
    class Meta:
        model = AudioComposition
        fields = ('title', 'author', 'photo', 'uncompressed_audio', 'is_published')

    # def clean_uncompressed_audio(self):
    #     audio_name = self.
    #     print(audio_name)
    #     return audio_name