from pathlib import Path
import pydub

from audio_test.models import AudioComposition
from Verstov_pro.settings import MEDIA_ROOT


def convert_to_mp3_and_save(pk: int):
    """ finds wav file via pk,
    convert wav file into 2 mp3 files (128k and 320к),
    save new files in DB """

    # find wav and open it
    db_object = AudioComposition.objects.get(pk=pk)
    wav_file = db_object.uncompressed_audio
    sound = pydub.AudioSegment.from_wav(wav_file.path)

    # making wav-file path
    folder_path, wav_name = wav_file.name.rsplit('/', 1)

    def save_mp3_and_return_mp3_path(bitrate):
        nonlocal folder_path, wav_name, sound

        name_mp3 = wav_name.rsplit('.', 1)[0] + f'_{bitrate}.mp3'
        path_mp3 = Path(MEDIA_ROOT, folder_path, name_mp3)
        sound.export(path_mp3, format="mp3", bitrate=f'{bitrate}k')
        return folder_path + '/' + name_mp3

    db_object.mp3_128.name = save_mp3_and_return_mp3_path(128)
    db_object.mp3_320.name = save_mp3_and_return_mp3_path(320)
    db_object.save()


