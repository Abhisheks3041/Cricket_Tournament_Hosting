# Generated by Django 4.2.6 on 2023-10-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_teams_usertype_teams_team_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='players',
            old_name='team_id',
            new_name='manager_id',
        ),
        migrations.RenameField(
            model_name='players',
            old_name='player_ph_no',
            new_name='player_phno',
        ),
        migrations.AddField(
            model_name='players',
            name='player_bg',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='player_quirk',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
