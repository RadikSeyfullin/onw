# Generated by Django 2.2.6 on 2019-11-01 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0007_travelmembers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelmembers',
            old_name='trevel_id',
            new_name='travel_id',
        ),
    ]