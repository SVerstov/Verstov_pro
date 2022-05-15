# Generated by Django 4.0.4 on 2022-04-15 23:02

import audio_test.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('photo', models.ImageField(blank=True, upload_to=audio_test.models.content_file_name, verbose_name='Обложка')),
                ('uncompressed_audio', models.FileField(upload_to=audio_test.models.content_file_name, validators=[django.core.validators.FileExtensionValidator(['wav'], 'Файлы с расширением “%(extension)s” не подходят. Пожалуйста загрузите файл с расширением : %(allowed_extensions)s.')], verbose_name='Несжатое аудио')),
                ('mp3_320', models.FileField(blank=True, upload_to=audio_test.models.content_file_name)),
                ('mp3_128', models.FileField(blank=True, upload_to=audio_test.models.content_file_name)),
                ('number_of_attempts', models.IntegerField(default=0)),
                ('number_of_correct_attempts', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headphones_attempts', models.IntegerField(default=0)),
                ('headphones_points', models.IntegerField(default=0)),
                ('speakers_attempts', models.IntegerField(default=0)),
                ('speakers_points', models.IntegerField(default=0)),
            ],
        ),
    ]