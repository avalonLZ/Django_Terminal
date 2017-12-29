# -*- coding:utf-8 -*-
"""Terminal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from MQTT_Terminal import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login/', views.Usr_Login),
    url(r'^outlogin/', views.Usr_OutLogin),
    #前端跳转：等于发出一个对跳转地址的一个GET请求
    #所以在views处理中还是直接render需要显示的界面即可
    url(r'^register/', views.register),
#    url(r'^register/$', account_views.register, name='register'),
    url(r'^bind_dev/', views.Bind_Dev),
]
