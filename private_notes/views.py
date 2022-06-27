from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.cache import cache
from .models import PrivateNotes
from services.crypto import get_short_id, encrypt_data, decrypt_data, get_random_chars

# TODO попробовать реализовать запрос дополнительного пароля без использования кэша


def create_private_note(request):
    """ Main app function.
    Render forms and obtain data"""

    if request.method == 'GET':
        # render app's main page
        return render(request, 'private_notes/new_private_note.html')
    elif request.method == 'POST':
        # obtain data from formsg
        user_note = request.POST.get('user_note')
        second_password = request.POST.get('second_password')
        # generate key
        password = get_random_chars(length=16)
        # encrypt user note
        encrypted_data = encrypt_data(user_note, password, second_password)
        # generate short id
        short_id = get_short_id(PrivateNotes)
        save_private_note(short_id, encrypted_data, second_password)

        # render success page
        messages.success(request, 'Ваша записка зашифрована и сохранена!')
        context = {'short_id': short_id, 'password': password}
        return render(request, 'private_notes/show_private_note_url.html', context)


def save_private_note(short_id, encrypted_data, second_password):
    """ Save encrypted note in database """
    obj = PrivateNotes()
    obj.short_id = short_id
    obj.encrypted_data = encrypted_data
    if second_password:
        # making a password exists tag
        obj.is_password = True
    obj.save()


def find_and_check_private_note(request, short_id, password):
    """ find the note and check if second password exists """
    if PrivateNotes.objects.filter(pk=short_id).exists():
        object_note = PrivateNotes.objects.get(pk=short_id)
        # check if note has a second password
        if object_note.is_password:
            # save some vars in cache
            cache.set(f'object_note_{short_id}', object_note)
            cache.set(f'password_{short_id}', password)
            # requesting the second password
            messages.warning(request, 'Записка зашифрована дополнительным паролем!')
            return redirect('second_password', short_id=short_id)
        return decrypt_and_show_private_note(request, object_note, password)
    else:
        messages.error(request, 'Записка не найдена!')
        return render(request, 'private_notes/new_private_note.html')


def decrypt_and_show_private_note(request, object_note, password, second_password=None):
    """ try to decrypt note. If success => show note and delete it from DB"""
    try:
        decrypted_data = decrypt_data(object_note.encrypted_data, password, second_password)
    except ValueError:
        # if decrypt failed render page with error
        messages.error(request, 'Ошибка расшифровки - ссылка или пароль не верны')
        return render(request, 'private_notes/new_private_note.html')
    # remove note from DB
    object_note.delete()
    # render page with decrypted note
    messages.warning(request, 'Записка удалена из базы данных. Если вам нужен этот текст - скопируйте его.')
    context = {'note': decrypted_data}
    return render(request, 'private_notes/show_decrypted_note.html', context)


def input_second_password(request, short_id):
    """ Get second password from user """
    if request.method == 'GET':
        return render(request, 'private_notes/input_second_password.html')
    elif request.method == 'POST':
        second_password = request.POST.get('second_password')
        # get objects from cache, clean cache
        object_note = cache.get(f'object_note_{short_id}')
        password = cache.get(f'password_{short_id}')
        return decrypt_and_show_private_note(request, object_note, password, second_password)
