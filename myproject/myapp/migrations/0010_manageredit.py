# Generated by Django 4.2.6 on 2023-10-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_team_id_players_manager_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='manageredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(default=0)),
            ],
        ),
    ]
