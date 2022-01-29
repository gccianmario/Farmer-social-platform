# Generated by Django 4.0 on 2022-01-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_remove_helprequest_slug_alter_helprequest_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('not_accepted', 'Not-accepted'), ('closed', 'Closed'), ('declined', 'Declined')], default='not_accepted', max_length=20),
        ),
    ]
