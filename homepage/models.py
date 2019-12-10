from __future__ import unicode_literals
from django.db import models


# Create your models here.
class   userInfo(models.Model):
    userId = models.CharField(primary_key=True, max_length=20, verbose_name='userId')
    userName = models.CharField(blank=True, max_length=20, verbose_name='userName')
    passWord = models.CharField(blank=True, max_length=20, verbose_name='passWord')
    Authority = models.CharField(blank=True, max_length=20, verbose_name='Authority')

    class Meta:
        managed = False
        db_table = 'userinfo'


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='homepage/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# データ制定
class noticeInfo(models.Model):
    userId = models.CharField(primary_key=True, max_length=20, verbose_name='userId')
    userName = models.CharField(blank=True, max_length=100, verbose_name='userName')
    userData = models.CharField(blank=True, max_length=100, verbose_name='userData')
    userCategory = models.CharField(blank=True, max_length=100, verbose_name='userCategory')
    userTitle = models.CharField(blank=True, max_length=100, verbose_name='userTitle')
    userContact = models.CharField(blank=True, max_length=100, verbose_name='userContact')
    userText = models.CharField(blank=True, max_length=200, verbose_name='userText')

    class Meta:
        managed = False
        db_table = 'noticeInfo'
