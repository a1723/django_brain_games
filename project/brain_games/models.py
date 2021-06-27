from django.db import models


# Create your models here.
class name(models.Model):
    name = models.CharField(max_length=25, db_index=True)