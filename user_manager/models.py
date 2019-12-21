from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import os
from .managers import CustomUserManager

def get_image_path(isinstance, filename):
    return os.path.join('images', 'users', str(isinstance.id), filename)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    country = models.CharField('Страна', null=True, max_length=20, blank=True)
    city = models.CharField('Город', null=True, max_length=20, blank=True)
    phone_number = models.CharField('Номер телефона', null=True, max_length=18, unique=True, blank=True)
    sex = models.CharField('Пол', max_length=5, choices=(('man', 'Мужской'),('women','Женский')), default='man')
    avatar = models.ImageField(upload_to=get_image_path, default='/images/users/default.png', verbose_name='Аватар')
    website_url = models.URLField(max_length=200, blank=True, default='https://onaway.ru/', verbose_name='Вебсайт')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
