from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    avatar = models.CharField(max_length=60)
    regDate = models.DateField('auto_now_add')
    
class Comment(models.Model):
    content = models.CharField(max_length=1000)
    postTime = models.DateTimeField('auto_now_add')
    followId = models.IntegerField(null=True)
    user = models.ForeignKey('User')
    