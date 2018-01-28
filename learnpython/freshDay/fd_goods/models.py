# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='fd_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()
    gbrief = models.CharField(max_length=255)
    gstock = models.IntegerField()
    gcontent = HTMLField()
    #gadv = models.BooleanField(default=False)
    gtype = models.ForeignKey(TypeInfo)


