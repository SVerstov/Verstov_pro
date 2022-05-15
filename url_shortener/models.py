from django.db import models


class ShortenerFields(models.Model):
    """ Describes fields """
    full_url = models.URLField(max_length=1000)
    short_id = models.CharField(max_length=6, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.full_url
