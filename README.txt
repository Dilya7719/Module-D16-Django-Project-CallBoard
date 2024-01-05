1. Приложение доступно по ссылке http://127.0.0.1:8000/calls/

2. логин/пароль админа     admin7719 / admin7719

3. для удобства тестирования у всех пользователей в приложении установлен пароль 123321asd

4. В файле CallBoard\CallBoard\settings.py необходимо внести свои значения для переменных ниже.

EMAIL_HOST_USER = "example@yandex.ru"
EMAIL_HOST_PASSWORD = "iliezvcovrxqizez"
DEFAULT_FROM_EMAIL = "example@yandex.ru"
SERVER_EMAIL = "example@yandex.ru"

5. Настроен вывод отправляемых писем в консоль.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'   #печать писем в консоль
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

6. Для работы приложения необходимо установить следующие пакеты:
pip install django
python -m pip install django-filter
pip install django-allauth
python -m pip install Pillow