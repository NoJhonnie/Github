from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey('fd_user.UserInfo')
    goods = models.ForeignKey('fd_goods.GoodsInfo')
    count = models.IntegerField()
