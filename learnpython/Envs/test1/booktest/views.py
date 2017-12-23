from django.shortcuts import render
from django.http import *
from .models import *
#from django.template import RequestContext,loader

def index(request):
    booklist = BookInfo.objects.all()
    context = {'title':booklist}
    return render(request,'booktest/index.html', context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list':herolist}
    return render(request,'booktest/show.html',context)