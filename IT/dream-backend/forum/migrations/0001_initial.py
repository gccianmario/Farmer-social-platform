# Generated by Django 4.0 on 2022-01-24 10:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=250)),
                ('text_body', models.TextField()),
                ('area', models.CharField(default='area', max_length=250)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('is_star', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_Tips', to='users.customuser')),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='forum.category')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=250)),
                ('text_body', models.TextField()),
                ('area', models.CharField(default='area', max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_Questions', to='users.customuser')),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='forum.category')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
