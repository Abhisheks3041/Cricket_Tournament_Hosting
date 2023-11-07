from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phonenumber=models.BigIntegerField(default=0,null=True)
    address=models.CharField(max_length=15,null=True)
    usertype=models.IntegerField(default=1)
    team_status=models.IntegerField(default=0)
    team_manager_status=models.IntegerField(default=0)
    
    
    
class Teams(models.Model):
    team_name=models.CharField(max_length=15,null=True)
    team_logo=models.FileField(null=True)
    manager_id=models.IntegerField(null=True,)
    
class Players(models.Model):
    player_name=models.CharField(max_length=15,null=True)
    player_quirk=models.CharField(max_length=15,null=True)
    player_bg=models.CharField(max_length=15,null=True)
    player_age=models.IntegerField(default=0)
    player_phno=models.BigIntegerField(default=0)
    manager_id=models.IntegerField(null=True)
 
    
    
class Messages(models.Model):
    your_name=models.CharField(max_length=15,null=True)
    your_email=models.EmailField    
    messages=models.TextField

class Tournament(models.Model):
    tournament_name=models.CharField(max_length=20,null=0)
    prize_money=models.IntegerField(null=0)
    team_participate=models.IntegerField(null=0)
    
    
    
    

    
    