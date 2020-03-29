from django.contrib import admin
from HanziModel.models import ZywTHz, Oftenhz, Passages
# Register your models here.

class ZywTHzAdmin(admin.ModelAdmin):
	list_display = ('id', 'chinese', 'sum', 'stroke', 'pinyin1', 'pinyin2', 'tone') #一行中显示的东西
	search_fields = ('tone','id', 'chinese', 'sum', 'stroke', 'pinyin1', 'pinyin2') #搜索栏可以搜索的索引

class PassagesAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'path') #一行中显示的东西
	search_fields = ('id', 'name') #搜索栏可以搜索的索引

admin.site.register(ZywTHz, ZywTHzAdmin)
admin.site.register(Oftenhz, ZywTHzAdmin)
admin.site.register(Passages, PassagesAdmin)