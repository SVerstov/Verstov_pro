### Проект содержит несколько веб приложений:
* Интерактивный Аудиотест (различить на слух wav и mp3)
* Сокращатель ссылок
* Секретные записки

**В работе сайт можно посмотреть тут:** https://Verstov.pro

### Запуск на локальном ПК:

* Установить нужные пакеты`pip install -r .\requirements.txt`
* Переименовать `editthis.env` > `.env`
* Редактировать `.env` не обязательно (тогда будет использован sqlite) 
 `SITE_ON_SERVER = False` означает, что будет использовать sqlite, `True` - postgres
* сделать миграции `python manage.py makemigrations`
* создать суперпользователя `python manage.py createsuperuser`
* Запустить `redis-server`
* Запустить celery `celery -A Verstov_pro worker -l info`
* Запустить локальный сервер `python manage.py runserver 0.0.0.0:8000`


Для добавления аудиотестов:
В админке `localhost:8000/admin/` можно добавить WAV файлы, конвертация в mp3 произойдёт автоматически
