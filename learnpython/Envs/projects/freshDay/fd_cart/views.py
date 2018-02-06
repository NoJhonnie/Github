# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import JsonResponse
from fd_user import user_decorator
from models import *


def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)

    context = {'title': "购物车",
               'page_name': 1 ,
               'carts': carts
               }
    return render(request, 'fd_cart/cart.html',context)


@user_decorator.login
def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)

    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count += count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')

# this is counting for the number of cart
def tcount(request):
    if request.is_ajax():
        uid = request.session['user_id']
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})

@user_decorator.login
def edit(request,cart_id,count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.count = int(count)
        count1 = cart.count
        cart.save()
        data = {'ok':0}
    except Exception as e:
        data = {'ok':count1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok':1}
    except Exception as e:
        data = {'ok':0}
    return JsonResponse(data)