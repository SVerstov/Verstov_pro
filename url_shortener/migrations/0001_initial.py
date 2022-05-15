# Generated by Django 4.0.3 on 2022-03-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('full_url', models.URLField()),
                ('short_id', models.URLField(max_length=6, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]