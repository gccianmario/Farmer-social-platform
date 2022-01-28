# Generated by Django 4.0 on 2022-01-27 19:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_remove_tip_dislikes_tip_dislikes_remove_tip_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='answer',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='user_dislikes_answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes_answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tip',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='user_dislikes_tip', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tip',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes_tip', to=settings.AUTH_USER_MODEL),
        ),
    ]