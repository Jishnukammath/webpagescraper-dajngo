from django.db import models

# Create your models here.

class word_count(models.Model):
    currentLink=models.CharField(max_length=500)
    wordCount=models.IntegerField()
    links=models.CharField(max_length=1000)
    mediaLinks=models.CharField(max_length=1000)
    fav=models.BooleanField(default=False)