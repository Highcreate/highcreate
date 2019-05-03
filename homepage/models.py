from django.db import models

# Create your models here.
class userInfo(models.Model):
     userName = models.CharField(primary_key=True, max_length=20, verbose_name='userName')
     passWord = models.CharField(blank=True, max_length=20, verbose_name='passWord')

     class Meta:
         managed = False
         db_table = 'userinfo'