# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render
from django.core.paginator import Paginator,Page

def index(request):
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type00 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type22 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type33 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type44 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type55 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {'title':'首页', 'guest_cart':1,
               'type0': type0, 'type00': type00,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type22': type22,
               'type3': type3, 'type33': type33,
               'type4': type4, 'type44': type44,
               'type5': type5, 'type55': type55,
               }
    return render(request, 'fd_goods/index.html', context)

def list(request,tid,pindex,sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(pindex))
    context = {
            'title':typeinfo.ttitle, 'guest_cart':1,
            'page':page,
            'paginator':paginator,
            'typeinfo':typeinfo,
            'sort':sort,
            'news':news
            }
    return render(request,'fd_goods/list.html',context)

def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick += 1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'title':goods.gtype.ttitle,'guest_cart':1,
               'g':goods, 'news':news, 'id':id}
    return render(request,'fd_goods/detail.html', context)