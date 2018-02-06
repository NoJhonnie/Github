from django.shortcuts import render
from models import *
from django.db import transaction
from fd_user import user_decorator


def order(request):
    pass

'''
事务：
1、创建订单对象
2、判断商品的库存
3、创建详单对象
4、修改商品信息
5、删除购物车
'''
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
    return render(request, 'fd_oder/pay.html',context)
