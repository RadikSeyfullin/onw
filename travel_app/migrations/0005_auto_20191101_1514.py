# Generated by Django 2.2.6 on 2019-11-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0004_travel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
