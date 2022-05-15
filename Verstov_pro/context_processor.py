from django.conf import settings

def root_url(request):
    """Get root url adress"""
    return {'SITE_URL': request.build_absolute_uri('/')}
