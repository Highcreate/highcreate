"""highcreate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Business/', views.business, name='business'),
    path('Corporation/', views.corporation, name='corporation'),
    path('Security/', views.security, name='security'),
    path('Workwithus/', views.workwithus, name='workwithus'),
    path('Employee/', views.Employee, name='Employee'),
    path('Contactus/', views.contactus, name='contactus'),
    path('Access/', views.access, name='access'),
    path('Profile/', views.profile, name='profile'),
    path('History/', views.history, name='history'),
    path('Philosophy/', views.philosophy, name='philosophy'),
    path('Engineering/', views.engineering, name='engineering'),
    path('Development/', views.development, name='development'),
    path('SendMail/', views.sendmail, name='sendmail'),
    path('matuyaindex/', views.matuya_index),
    path('detail/', views.detail),
    path('detail/<int:matuyaId>', views.get_detail),
    path('details/<int:matuyaId>', views.get_details),
    path('matuyaadd/', views.data_add),
    path('delete/', views.data_delete),
    path('select/', views.select)
]
