# Generated by Django 4.0.3 on 2022-03-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_shortenerfields_delete_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenerfields',
            name='full_url',
            field=models.URLField(max_length=1000),
        ),
    ]