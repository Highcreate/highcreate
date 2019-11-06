# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from homepage import models,forms
import json

#login画面
def login(request):
    return render(request, 'login.html')

#社員情報画面
def employinfo(request):
    return render(request, 'employinfo.html')

#社内通知画面
def notice(request):
    return render(request, 'notice.html')

#勤務情報画面
def workinfo(request):
    return render(request, 'workinfo.html')


# 保存数据
@csrf_exempt
def add(request):
    username = request.POST['userName']
    password = request.POST['passWord']
    #models.userInfo.objects.create(username=username, password=password)
    #return render(request, 'index.html')
    userInfo = models.userInfo()
    if len(username) > 0:
        print("id不是null")
        userInfo.userName = username

    userInfo.passWord = password
    userInfo.save()
    userInfos = models.userInfo.objects.all()
    return HttpResponseRedirect("/index")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        mylife = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(mylife.name, mylife)
        upload_file_url =fs.url(filename)
        return render(request,'homepage/simple_upload.html', {
            'uploaded_file_url':upload_file_url
        })
    return render(request,'homepage/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('')
    else:
        form = forms.DocumentForm()
    return render(request,'homepage/model_form_upload.html',{
        'form':form
    })