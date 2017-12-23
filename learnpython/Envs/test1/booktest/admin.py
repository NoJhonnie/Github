from django.contrib import admin
from models import *

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','btitile','bpub_date']
    search_fields = ['btitile']
    fieldsets = [
        ('base',{'fields':['btitile']}),
        ('more',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)