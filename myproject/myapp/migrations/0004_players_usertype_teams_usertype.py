# Generated by Django 4.2.6 on 2023-10-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_messages_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='usertype',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='teams',
            name='usertype',
            field=models.IntegerField(default=1),
        ),
    ]
