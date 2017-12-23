from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitile = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.btitile.encode('utf-8')

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
    def __str__(self):
        return self.hname.encode('utf-8')

