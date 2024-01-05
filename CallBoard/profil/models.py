from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    """ Данные пользователей """
    woman = 'W'
    man = 'M'
    GENDER_TYPES_LIST = [
        (woman, 'Женщина'),
        (man, 'Мужчина')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=16, unique=False)
    surname = models.CharField(max_length=32, unique=False)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES_LIST, default=man)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.surname}"
