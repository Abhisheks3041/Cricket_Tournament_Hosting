# Generated by Django 4.2.6 on 2023-10-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_user_type_user_usertype_remove_user_ph_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='team_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='manager_id',
            field=models.IntegerField(null=True),
        ),
    ]