# Generated by Django 4.0 on 2022-01-26 20:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_alter_question_area_alter_tip_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tip',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='tip',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='user_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='tip',
            name='likes',
        ),
        migrations.AddField(
            model_name='tip',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
