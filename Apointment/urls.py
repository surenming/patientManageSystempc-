#coding: utf8
"""Apointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import xadmin
from django.conf.urls import url,include
from django.contrib import admin


from apoint.Views.userView import *
from apoint.Views.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index$',index),
    url(r'^login',userlogin),
    url(r'^',include('apoint.adminurls')),#PC端接口
    url(r'^api/apoint/',include('apoint.wx_urls')),#微信调用接口
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),

    url(r'^renling$',renling),
    url(r'^createUser$',createUser),
    url(r'^renlingAction$',renlingAction),
    url(r'pations$',pations),
    url(r'^pationsview',pationsview),#客服患者数据
    url(r'^remind',remind),
    url(r'^account',account),
    url(r'^addpation',addpation),
    url(r'^chart$',chart),
    url(r'^upload',uploader),
    url(r'^orderdetail$',orderdetail),
    url(r'^ordersubmit',OrderSubmit),
    url(r'^orderupdate',OrderUpdte),
    url(r'^staffaddnew', staffaddnew),
]
