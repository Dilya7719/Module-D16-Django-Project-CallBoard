from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Respond


@receiver(post_save, sender=Respond)
def respond_created(instance, created, **kwargs):
    if created:
        email = User.objects.get(id=instance.respond_call.call_author.id).email
        subject = f'Новый отклик к вашему объявлению {instance.respond_call.call_header}'
        text_content = (
            f'Новый отклик к вашему объявлению {instance.respond_call.call_header}\n\n'
            f'Текст отклика: {instance.respond_text}\n\n'
            f'Ссылка на объявление: http://127.0.0.1:8000{instance.respond_call.get_absolute_url()}'
        )
        html_content = (
            f'Новый отклик к вашему объявлению {instance.respond_call.call_header}<br><br>'
            f'Текст отклика: {instance.respond_text}<br><br>'
            f'<a href="http://127.0.0.1:8000{instance.respond_call.get_absolute_url()}">'
            f'Ссылка на объявление</a>'
        )
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    else:
        email = User.objects.get(id=instance.respond_author.id).email
        subject = f'Изменение статуса вашего отклика к объявлению {instance.respond_call.call_header}'
        if instance.respond_accept:
            status = 'Принят'
        else:
            status = 'Отклонен'
        text_content = (
            f'Изменение статуса вашего отклика к объявлению {instance.respond_call.call_header}\n\n'
            f'Текст отклика: {instance.respond_text}\n'
            f'Статус отклика: {status}\n\n'
            f'Ссылка на объявление: http://127.0.0.1:8000{instance.respond_call.get_absolute_url()}'
        )
        html_content = (
            f'Изменение статуса вашего отклика к объявлению {instance.respond_call.call_header}<br><br>'
            f'Текст отклика: {instance.respond_text}<br>'
            f'Статус отклика: {status}<br><br>'
            f'<a href="http://127.0.0.1:8000{instance.respond_call.get_absolute_url()}">'
            f'Ссылка на объявление</a>'
        )
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
