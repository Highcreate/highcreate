from __future__ import unicode_literals
from django.db import models


# Create your models here.
class userInfo(models.Model):
     userName = models.CharField(primary_key=True, max_length=20, verbose_name='userName')
     passWord = models.CharField(blank=True, max_length=20, verbose_name='passWord')

     class Meta:
         managed = False
         db_table = 'userinfo'

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='homepage/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)