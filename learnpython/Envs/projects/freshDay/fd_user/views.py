# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import user_decorator
from models import *
from fd_goods.models import GoodsInfo
from hashlib import sha1
from django.shortcuts import render,redirect,HttpResponseRedirect

def register(request):
    context = {'title':'用户注册'}
    return render(request,'fd_user/register.html',context)

def register_handle(request):
    #receriver input information
    post = request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email')
    #jugle password
    if pwd != cpwd:
        return redirect('/user/register/')
    #encrypt password
    s1 = sha1()
    s1.update(pwd)
    upwd = s1.hexdigest()

    #create user
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    user.save()

    #success redirect the login
    return redirect('/user/login/')

def login(request):
   uname = request.COOKIES.get('uname', '')
   context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
   return render(request,'fd_user/login.html',context)

def login_handle(request):
    get = request.POST
    uname = get.get('username')
    upwd = get.get('pwd')
    rm = get.get('rm',0)

    #according username searching
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)

            #remember it
            if rm != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'fd_user/login.html',context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'fd_user/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail

    goods_ids = request.COOKIES.get('goods_ids','')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {'title': '用户中心', 'page_name':1,
               'user_email': user_email,
               'user_name': request.session['user_name'],
               'goods_list': goods_list
               }
    return render(request, 'fd_user/user_center_info.html', context)

@user_decorator.login
def order(request):
    context = {'title': '用户中心', 'page_name':1}
    return render(request, 'fd_user/user_center_order.html', context)

@user_decorator.login
def site(request):
    context = {'title': '用户中心', 'page_name':1}
    return render(request, 'fd_user/user_center_site.html', context)