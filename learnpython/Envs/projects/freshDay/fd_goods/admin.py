# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *

from django.contrib import admin

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'isDelete', 'gtitle', 'gprice', 'gunit', 'gclick', 'gstock', 'gbrief', 'gcontent']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)