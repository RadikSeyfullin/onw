# Generated by Django 2.2.6 on 2019-11-01 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_auto_20191101_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='creator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='end_date',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
