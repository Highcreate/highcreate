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
from  homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Business/', views.business, name='business'),
    path('Corporation/', views.corporation, name='corporation'),
    path('Security/', views.security, name='security'),
    path('Workwithus/', views.workwithus, name='workwithus'),
    path('Contactus/', views.contactus, name='contactus'),
    path('saved_resource/', views.saved_resource, name='saved_resource'),
    path('simpleupload/', views.simple_upload, name='simple_upload'),
    path('fromupload/', views.model_form_upload, name='model_form_upload'),
]