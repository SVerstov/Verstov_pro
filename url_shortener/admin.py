from django.contrib import admin
from .models import ShortenerFields


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'full_url', 'created_at', 'count')
    ordering = ('-created_at',)


admin.site.register(ShortenerFields, UrlsAdmin)
