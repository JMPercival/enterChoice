from django.db import models

# Create your models here.
class Choices(models.Model):
    id = models.AutoField(primary_key=True)
    choice = models.TextField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()
    trigger = models.IntegerField(default=1)
    
class Rolls(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.IntegerField()
    end = models.IntegerField()
    randomRoll = models.IntegerField()
    trigger = models.IntegerField(default=1) 
    