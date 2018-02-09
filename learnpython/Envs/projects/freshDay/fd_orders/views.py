# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import *
from fd_cart.models import CartInfo
from fd_user import models
from django.db import transaction
from fd_user import user_decorator
from datetime import datetime
from decimal import Decimal

@user_decorator.login
def order(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)

    context = {'title':'提交订单','page_name':1,'carts':carts}
    return render(request, 'fd_orders/place_order.html',context)


@transaction.atomic()
@user_decorator.login
def order_handle(request):
    tran_id = transaction.savepoint()
    cart_ids = request.POST.get('cart_ids')
    try:
        order = OrderInfo()
        nowtime = datetime.now()
        uid = request.session['user_id']
        order.oid = '%s%d'%(nowtime.strftime('%Y%m%d%H%M%S'),uid)
        order.user_id = uid
        order.odate = nowtime
        order.ototal = Decimal(request.POST.get('total'))
        order.save()

        #创建详单对象
        cart_ids1 = [int(item) for item in cart_ids.split(',')]
        for id1 in cart_ids1:
            detail = OrderDetailInfo()
            detail.order = order
            cart = CartInfo.objects.get(id=id1)
            goods = cart.goods
            if goods.gstock >= cart.count:
                goods.gstock = cart.goods.gstock - cart.count
                goods.save()
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print '===============%s' %e
        transaction.savepoint_rollback(tran_id)

    return redirect('/user/order/')


@user_decorator.login
def pay(request,id):
    oder = OrderInfo.objects.get(oid = id)
    order.oIsPay = True
    order.save()
    context = {'order':order}
    return render(request, 'fd_orders/pay.html',context)
