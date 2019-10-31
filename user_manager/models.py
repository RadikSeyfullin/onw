from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(null=True, max_length=20, blank=True)
    city = models.CharField(null=True, max_length=20, blank=True)
    phone_number = models.CharField(null=True, max_length=18, unique=True, blank=True)
    sex = models.CharField(max_length=5, choices=(('man', 'Мужской'),('women','Женский')), default='man')
    avatar = models.ImageField(upload_to='users', default='static/images/users/default_logo.png', verbose_name='Аватар')
    website_url = models.URLField(max_length=200, blank=True, default='https://onaway.ru/')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
