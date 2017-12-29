# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from MQTT_Terminal.models import TbDev
from django.contrib import auth
# Create your views here.


def Get_Dev_Name_List(temp):
    td_name = []
    for i in range(0, len(temp)):
        td_name.append(re.findall(r'\d\d\d\d', str(temp[i]))[0])
    return td_name


#要求用户登录，若没登录则跳转到LOGIN_URL设置的地址中,此处跳转到登录界面
@login_required
def index(req):
    displaylist = TbDev.objects.all()
    dev_name = Get_Dev_Name_List(displaylist.values_list('device_name_foreign'))
    selectlist = sorted(set(dev_name),key=dev_name.index)
    if req.method == "POST":
        str_dev_name = str(req.POST.get('dev_name_select'))#表单以字典形式传入
        needdata = displaylist.filter(device_name_foreign = str_dev_name)#和form中的元素name属性相同
        filter_dev_name = []
        for i in range(0, len(dev_name)):
            if dev_name[i] == str_dev_name and str_dev_name != '99999':
                filter_dev_name.append(dev_name[i])
            elif str_dev_name == '99999':
                filter_dev_name = dev_name
                needdata = displaylist
        return render_to_response('index.html', {'user' : auth.get_user(req),'names': needdata, 'dev_name': selectlist,
                                                 'dev_name_list':filter_dev_name})
    return render_to_response('index.html', {'user' : auth.get_user(req),'names': displaylist, 'dev_name': selectlist,
                                             'dev_name_list':dev_name})

@login_required
def Bind_Dev(req):
    pass
    return HttpResponseRedirect('/')

#退出当前用户，重定向到登录界面
@login_required
def Usr_OutLogin(req):
    auth.logout(req)
    return HttpResponseRedirect('/login')


def Usr_Login(req):
    user_pw_error = '0'

    if req.method == "POST":
        username = req.POST['username']
        pw = req.POST['password']
        user = auth.authenticate(username=username, password=pw)
        if user is None:
            #失败直接返回登录界面，成功则重定向
            user_pw_error = '1'
            return render_to_response('login.html', {'user_pw_error': user_pw_error})
        else:
            #加入此才会在跳转后依然保持登录状态，用了session
            auth.login(req, user)
            #重定向，需要在url中添加相应url，否则无法找到
            #重定向会有一个get而render_to_response返回网页是没有get的
            return HttpResponseRedirect('/')
    elif req.method == 'GET':
        return render_to_response('login.html', {'user_pw_error': user_pw_error})



def register(req):
    User.objects.create_superuser('')
    messages.error(req, '用户或密码错误', extra_tags='bg-warning text-warning')
    return render(req,'register.html')


