from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25, db_index=True),
    
    
class answer(models.Model):    
    answer = models.CharField(max_length=25, db_index=True)