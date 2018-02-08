# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
from fd_cart.models import CartInfo
from django.db import transaction
from fd_user import user_decorator


def order(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)

    context = {'title':'提交订单','page_name':1,'carts':carts}
    return render(request, 'fd_orders/place_order.html',context)


@transaction.atomic()
@user_decorator.login
def order_handle(request):
    pass

@user_decorator.login
def pay(request,id):
    oder = OrderInfo.objects.get(oid = id)
    order.oIsPay = True
    order.save()
    context = {'order':order}
    return render(request, 'fd_orders/pay.html',context)
