from django.shortcuts import render
from . import models
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.template.response import TemplateResponse

def index(request):
    userInfos = models.userInfo.objects.all()
    return render(request, 'index.html', {'userinfos':userInfos})


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
        userInfo.userName = username;

    userInfo.passWord = password
    userInfo.save()
    userInfos = models.userInfo.objects.all()
    return HttpResponseRedirect("/index")
