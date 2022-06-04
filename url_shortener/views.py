from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import ObjectDoesNotExist
from .models import ShortenerFields
from .forms import ShortenerForm
from services.crypto import get_short_id


def shortener(request):
    if request.method == 'GET':
        return render_shortener_main_page(request)
    elif request.method == 'POST':
        # get user input (url)
        full_url = request.POST.get('full_url')
        # duplication check
        if ShortenerFields.objects.filter(full_url=full_url).exists():
            # return short_id from DB if duplicate exists
            obj = ShortenerFields.objects.get(full_url=full_url)
            # return short_id from DB without generation
            context = {'short_id': obj.pk}
        else:
            short_id = get_short_id(Fields=ShortenerFields)
            obj = ShortenerFields()
            obj.full_url = full_url
            obj.short_id = short_id
            obj.save()
            context = {'short_id': short_id}

        messages.success(request, 'Ваша ссылка создана! ')
        return render(request, 'url_shortener/get_short_url.html', context)


def redirect_to_main_url(request, short_id):
    """ redirect to target URL if short_id exists"""
    try:
        redirect_obj = ShortenerFields.objects.get(pk=short_id)
        redirect_obj.count += 1
        redirect_obj.save()
        return HttpResponseRedirect(redirect_obj.full_url)
    except ObjectDoesNotExist:
        # redirect to app's main page with error message
        messages.error(request, 'Ссылка не найдена!')
        return render_shortener_main_page(request)


def render_shortener_main_page(request):
    form = ShortenerForm()
    context = {'form': form}
    return render(request, 'url_shortener/shortener.html', context)
