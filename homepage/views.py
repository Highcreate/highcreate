# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from email.header import Header
from email.mime.text import MIMEText
import base64
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from homepage import models, forms
import json

from django.core.paginator import Paginator

# URL遷移
accessHLink = 'href=/Access/'
profileHLink = 'href=/Profile/'
historyHLink = 'href=/History/'
philosophyHLink = 'href=/Philosophy/'
engineeringHLink = 'href=/Engineering/'
developmentHLink = 'href=/Development/'
securityHLink = 'href=/Security/'
workwithusHLink = 'href=/Workwithus/'
contactusHLink = 'href=/Contactus/'
# js遷移
accessNLink = 'ng-click=gotoBottom(\'map-content\')'
profileNLink = 'ng-click=gotoBottom(\'company-profile\')'
historyNLink = 'ng-click=gotoBottom(\'history\')'
philosophyNLink = 'ng-click=gotoBottom(\'management-philosophy\')'
engineeringNLink = 'ng-click=gotoBottom(\'engineering\')'
developmentNLink = 'ng-click=gotoBottom(\'development\')'
securityNLink = 'ng-click=gotoBottom(\'security\')'
workwithusNLink = 'ng-click=gotoBottom(\'workwithus\')'
contactusNLink = 'ng-click=gotoBottom(\'contactus\')'


# main画面
def index(request):
    return render(request, 'index.html', {
        'accessLink': accessNLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# アクセス画面
def access(request):
    jumpflag = 'map-content'
    return render(request, 'index.html', {
        'jumpflag': jumpflag,
        'accessLink': accessNLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 会社情報画面
def corporation(request):
    return render(request, 'corporation.html', {
        'accessLink': accessHLink,
        'profileLink': profileNLink,
        'historyLink': historyNLink,
        'philosophyLink': philosophyNLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 会社概要画面
def profile(request):
    jumpflag = 'company-profile'
    return render(request, 'corporation.html', {
        'jumpflag': jumpflag,
        'accessLink': accessHLink,
        'profileLink': profileNLink,
        'historyLink': historyNLink,
        'philosophyLink': philosophyNLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 沿革画面
def history(request):
    jumpflag = 'history'
    return render(request, 'corporation.html', {
        'jumpflag': jumpflag,
        'accessLink': accessHLink,
        'profileLink': profileNLink,
        'historyLink': historyNLink,
        'philosophyLink': philosophyNLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 経営理念画面
def philosophy(request):
    jumpflag = 'management-philosophy'
    return render(request, 'corporation.html', {
        'jumpflag': jumpflag,
        'accessLink': accessHLink,
        'profileLink': profileNLink,
        'historyLink': historyNLink,
        'philosophyLink': philosophyNLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 事業内容画面
def business(request):
    return render(request, 'business.html', {
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringNLink,
        'developmentLink': developmentNLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# システムエンジニアリング画面
def engineering(request):
    jumpflag = 'engineering'
    return render(request, 'business.html', {
        'jumpflag': jumpflag,
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringNLink,
        'developmentLink': developmentNLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# システム開発・保守・運用画面
def development(request):
    jumpflag = 'development'
    return render(request, 'business.html', {
        'jumpflag': jumpflag,
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringNLink,
        'developmentLink': developmentNLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 個人情報保護方針画面
def security(request):
    return render(request, 'Security.html', {
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityNLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusHLink
    })


# 採用情報画面
def workwithus(request):
    return render(request, 'Work_With_Us.html', {
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusNLink,
        'contactusLink': contactusHLink
    })


def Employee(request):
    return render(request, 'Employee_Voice.html', {
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusNLink,
        'num': range(10)
    })


# お問い合わせ画面
def contactus(request):
    return render(request, 'Contact_Us.html', {
        'accessLink': accessHLink,
        'profileLink': profileHLink,
        'historyLink': historyHLink,
        'philosophyLink': philosophyHLink,
        'engineeringLink': engineeringHLink,
        'developmentLink': developmentHLink,
        'securityLink': securityHLink,
        'workwithusLink': workwithusHLink,
        'contactusLink': contactusNLink
    })


@csrf_exempt
def sendmail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject = data.get('company', None)
        message = data.get('text', None)
        from_email = data.get('fromemail', None)
        recipient_list = ["info@highcreate.co.jp"]
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'Contact_Us.html', {
            'accessLink': accessHLink,
            'profileLink': profileHLink,
            'historyLink': historyHLink,
            'philosophyLink': philosophyHLink,
            'engineeringLink': engineeringHLink,
            'developmentLink': developmentHLink,
            'securityLink': securityHLink,
            'workwithusLink': workwithusHLink,
            'contactusLink': contactusNLink
        })


# 对送骨保密画面
def matuya_index(request):
    inclubInfos = models.inclubInfo.objects.all()
    return render(request, 'matuyaindex.html',
                  {
                      'inclubinfos': inclubInfos
                  }
                  )


# 全てデータ一览画面
def detail(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print(page)
    detail_info = models.inclubInfo.objects.all()

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

    return render(request, 'detail.html',
                  {
                      'detail_info': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page
                  }
                  )


# 社内通知編集画面
def get_detail(request, matuyaId):
    inclubInfos = models.inclubInfo.objects.all()
    detail_info = None
    for inclubInfo in inclubInfos:
        if inclubInfo.matuyaId == matuyaId:
            detail_info = inclubInfo
            break

    return render(request, 'getdetail.html',
                  {
                      'detail_info': detail_info
                  }
                  )


# 社内通知详细画面
def get_details(request, matuyaId):
    inclubInfos = models.inclubInfo.objects.all()
    detail_info = None
    for inclubInfo in inclubInfos:
        if inclubInfo.matuyaId == matuyaId:
            detail_info = inclubInfo
            break

    return render(request, 'getdetails.html',
                  {
                      'detail_info': detail_info
                  }
                  )


# データ保存
@csrf_exempt
def data_add(request):
    matuyaid = request.POST['matuyaId']
    matuyadata = request.POST['matuyaData']
    matuyacategory = request.POST['matuyaCategory']
    matuyatitle = request.POST['matuyaTitle']
    matuyacontact = request.POST['matuyaContact']
    matuyatext = request.POST['matuyaText']

    inclubInfo = models.inclubInfo()
    if len(matuyaid) > 0:
        print("id不是null")
        inclubInfo.matuyaId = matuyaid
    inclubInfo.matuyaData = matuyadata
    inclubInfo.matuyaCategory = matuyacategory
    inclubInfo.matuyaTitle = matuyatitle
    inclubInfo.matuyaContact = matuyacontact
    inclubInfo.matuyaText = matuyatext

    inclubInfo.save()

    return HttpResponseRedirect("/detail")


# データ削除
@csrf_exempt
def data_delete(request):
    matuyaid = request.POST['matuyaId']
    inclubInfo = models.inclubInfo()
    if len(matuyaid) > 0:
        print("id不是null")
        inclubInfo.matuyaId = matuyaid

    inclubInfo.delete()

    return HttpResponseRedirect("/detail")


# 検索
def select(request):
    matuyaid = request.GET['matuyaId']

    # id検索
    user_select = models.inclubInfo.objects.get(matuyaId=matuyaid)

    return render(request, 'select.html',
                  {
                      'user_select': user_select
                  }
                  )
