from django.db import models
from user_manager.models import CustomUser
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def get_image_path(isinstance, filename):
    return os.path.join('images', 'travels', str(isinstance.id), filename)

# Create your models here.
class Travel(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    start_date = models.DateField("Дата начала", auto_now=False)
    end_date = models.DateField("Дата окончания", auto_now=False)
    members = models.IntegerField("Количество участников", default=0)
    country = models.CharField("Страна", max_length=100)
    city = models.CharField("Город", max_length=100)
    creator_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Создатель")
    created_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name

class TravelMembers(models.Model):
    travel_id = models.ForeignKey(Travel, on_delete=models.CASCADE, verbose_name="Путешествие")
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
