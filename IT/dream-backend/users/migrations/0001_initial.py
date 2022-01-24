# Generated by Django 4.0 on 2022-01-24 11:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AuthCodePolicyMaker',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('isValid', models.BooleanField(default=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.district')),
            ],
        ),
        migrations.CreateModel(
            name='AuthCodeFarmer',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('isValid', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.area')),
            ],
        ),
        migrations.CreateModel(
            name='AuthCodeAgronomist',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('isValid', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.area')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.district'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('auth_code', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('role', models.CharField(default='no role', max_length=20)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.area')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.district')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
