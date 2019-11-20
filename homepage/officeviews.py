# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from homepage import models, forms
import json
# 分页插件
from django.core.paginator import Paginator


# login 画面登陆
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        user_obj = models.userInfo.objects.filter(userName=userName,
                                                  passWord=passWord
                                                  ).first()
        if user_obj:
            return HttpResponseRedirect("/employinfo")
        else:
            return HttpResponse('用户名或密码错误')


# 社員情報画面
def employinfo(request):
    return render(request, 'employinfo.html')


# 社内通知画面
def notice(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    # DB table完善后需要改
    detail_info = models.noticeInfo.objects.all()

    # 设置显示多少条信息
    paginator = Paginator(detail_info, 10)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'notice.html',
                  {
                      'detail_info': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page
                  }
                  )


# 社内通知編集画面
def modify_detail(request, userId):
    noticeInfos = models.noticeInfo.objects.all()
    detail_info = None
    for noticeInfo in noticeInfos:
        if noticeInfo.userId == userId:
            detail_info = noticeInfo
            break

    return render(request, 'modify_detail.html',
                  {
                      'detail_info': detail_info
                  }
                  )


# 社内通知详细画面
def detail(request, userId):
    noticeInfos = models.noticeInfo.objects.all()
    detail_info = None
    for noticeInfo in noticeInfos:
        if noticeInfo.userId == userId:
            detail_info = noticeInfo
            break

    return render(request, 'detail.html',
                  {
                      'detail_info': detail_info
                  }
                  )


# 勤務情報画面
def workinfo(request):
    return render(request, 'workinfo.html')


# 保存数据
@csrf_exempt
def add(request):
    username = request.POST['userName']
    password = request.POST['passWord']
    # models.userInfo.objects.create(username=username, password=password)
    # return render(request, 'index.html')
    userInfo = models.userInfo()
    if len(username) > 0:
        print("id不是null")
        userInfo.userName = username

    userInfo.passWord = password
    userInfo.save()
    userInfos = models.userInfo.objects.all()
    return HttpResponseRedirect("/index")


# 詳細データ保存
@csrf_exempt
def data_add(request):
    userid = request.POST['userId']
    userdata = request.POST['userData']
    usercategory = request.POST['userCategory']
    usertitle = request.POST['userTitle']
    usercontact = request.POST['userContact']
    usertext = request.POST['userText']

    noticeInfo = models.noticeInfo()
    noticeInfo.userId = userid
    noticeInfo.userData = userdata
    noticeInfo.userCategory = usercategory
    noticeInfo.userTitle = usertitle
    noticeInfo.userContact = usercontact
    noticeInfo.userText = usertext

    noticeInfo.save()

    return HttpResponseRedirect("/notice")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        mylife = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(mylife.name, mylife)
        upload_file_url = fs.url(filename)
        return render(request, 'homepage/simple_upload.html', {
            'uploaded_file_url': upload_file_url
        })
    return render(request, 'homepage/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = forms.DocumentForm()
    return render(request, 'homepage/model_form_upload.html', {
        'form': form
    })
