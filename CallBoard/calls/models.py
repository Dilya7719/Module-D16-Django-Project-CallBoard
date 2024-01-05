from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Call(models.Model):
    """ Объявления. """
    CATEGORIES_LIST = [
        ('tanks', 'Танки'),
        ('hills', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('gild_masters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potion_masters', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний'),
    ]
    call_author = models.ForeignKey(User, on_delete=models.CASCADE)
    call_create_date = models.DateTimeField(auto_now_add=True)
    call_category = models.CharField(max_length=14, choices=CATEGORIES_LIST, default='tanks')
    call_header = models.CharField(max_length=128)
    call_text = models.TextField()
    call_img = models.ImageField(upload_to='call', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f"Объявление от {self.call_create_date:%d.%m.%Y %H:%M} (запись №{self.id})"

    def get_absolute_url(self):
        return reverse('respond_send', args=[str(self.id)])

    def save(self):
        super().save()
        if self.call_img:
            img = Image.open(self.call_img.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.call_img.path)


class Respond(models.Model):
    """ Отклики к объявлениям. """
    respond_call = models.ForeignKey(Call, on_delete=models.CASCADE)
    respond_author = models.ForeignKey(User, on_delete=models.CASCADE)
    respond_text = models.TextField()
    respond_create_date = models.DateTimeField(auto_now_add=True)
    respond_accept = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.respond_call} {self.respond_text}'

