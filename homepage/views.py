# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from email.header import Header
from email.mime.text import MIMEText
import base64
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from homepage import models,forms
import json

#URL遷移
accessHLink = 'href=/Access/'
profileHLink = 'href=/Profile/'
historyHLink = 'href=/History/'
philosophyHLink = 'href=/Philosophy/'
engineeringHLink = 'href=/Engineering/'
developmentHLink = 'href=/Development/'
securityHLink = 'href=/Security/'
workwithusHLink = 'href=/Workwithus/'
contactusHLink = 'href=/Contactus/'
#js遷移
accessNLink = 'ng-click=gotoBottom(\'map-content\')'
profileNLink = 'ng-click=gotoBottom(\'company-profile\')'
historyNLink = 'ng-click=gotoBottom(\'history\')'
philosophyNLink = 'ng-click=gotoBottom(\'management-philosophy\')'
engineeringNLink = 'ng-click=gotoBottom(\'engineering\')'
developmentNLink = 'ng-click=gotoBottom(\'development\')'
securityNLink = 'ng-click=gotoBottom(\'security\')'
workwithusNLink = 'ng-click=gotoBottom(\'workwithus\')'
contactusNLink = 'ng-click=gotoBottom(\'contactus\')'

#main画面
def index(request):
    return render(request, 'index.html', {
        'accessLink':accessNLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#アクセス画面
def access(request):
    jumpflag = 'map-content'
    return render(request,'index.html',{
        'jumpflag':jumpflag ,
        'accessLink':accessNLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#会社情報画面
def corporation(request):
    return render(request, 'corporation.html', {
        'accessLink':accessHLink ,
        'profileLink':profileNLink ,
        'historyLink':historyNLink ,
        'philosophyLink':philosophyNLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#会社概要画面
def profile(request):
    jumpflag = 'company-profile'
    return render(request, 'corporation.html', {
        'jumpflag':jumpflag ,
        'accessLink':accessHLink ,
        'profileLink':profileNLink ,
        'historyLink':historyNLink ,
        'philosophyLink':philosophyNLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#沿革画面
def history(request):
    jumpflag = 'history'
    return render(request, 'corporation.html', {
        'jumpflag':jumpflag ,
        'accessLink':accessHLink ,
        'profileLink':profileNLink ,
        'historyLink':historyNLink ,
        'philosophyLink':philosophyNLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#経営理念画面
def philosophy(request):
    jumpflag = 'management-philosophy'
    return render(request, 'corporation.html', {
        'jumpflag':jumpflag ,
        'accessLink':accessHLink ,
        'profileLink':profileNLink ,
        'historyLink':historyNLink ,
        'philosophyLink':philosophyNLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#事業内容画面
def business(request):
    return render(request, 'business.html', {
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringNLink ,
        'developmentLink':developmentNLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#システムエンジニアリング画面
def engineering(request):
    jumpflag = 'engineering'
    return render(request, 'business.html', {
        'jumpflag':jumpflag ,
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringNLink ,
        'developmentLink':developmentNLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#システム開発・保守・運用画面
def development(request):
    jumpflag = 'development'
    return render(request, 'business.html', {
        'jumpflag':jumpflag ,
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringNLink ,
        'developmentLink':developmentNLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#個人情報保護方針画面
def security(request):
    return render(request, 'Security.html', {
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityNLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusHLink
        })

#採用情報画面
def workwithus(request):
    return render(request, 'Work_With_Us.html', {
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusNLink ,
        'contactusLink':contactusHLink
        })

def Employee(request):
    return render(request, 'Employee_Voice.html', {
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusNLink
        })

#お問い合わせ画面
def contactus(request):
    return render(request, 'Contact_Us.html', {
        'accessLink':accessHLink ,
        'profileLink':profileHLink ,
        'historyLink':historyHLink ,
        'philosophyLink':philosophyHLink ,
        'engineeringLink':engineeringHLink ,
        'developmentLink':developmentHLink ,
        'securityLink':securityHLink ,
        'workwithusLink':workwithusHLink ,
        'contactusLink':contactusNLink
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
            'accessLink':accessHLink ,
            'profileLink':profileHLink ,
            'historyLink':historyHLink ,
            'philosophyLink':philosophyHLink ,
            'engineeringLink':engineeringHLink ,
            'developmentLink':developmentHLink ,
            'securityLink':securityHLink ,
            'workwithusLink':workwithusHLink ,
            'contactusLink':contactusNLink
            })
