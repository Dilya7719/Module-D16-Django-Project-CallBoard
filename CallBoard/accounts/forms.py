from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.core.mail import mail_admins
from profil.models import UserData


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        user.username = user.email

        UserData.objects.create(user=user, name=user.email)

        send_mail(
            subject='Добро пожаловать на сайт Доска объявлений!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user

