from django.db import models


class PrivateNotes(models.Model):
    short_id = models.CharField(max_length=8, primary_key=True)
    encrypted_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    delete_date = models.DateTimeField(null=True)
    email = models.EmailField(blank=True)
    is_password = models.BooleanField(default=False)
