from django.shortcuts import render
from django.http import JsonResponse
from fd_user import user_decorator
from models import *

def cart(request):
    uid = request.session['user.id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'title':购物车,
               'page_num':1,
               'carts':carts
               }
    return  render(request,'fd_cart/cart.html',context)

@user_decorator.login
def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)