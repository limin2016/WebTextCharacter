from django.db import models
from myapp.models import Struts
from django.http import HttpResponse
import json


def transfer(request):	
	startX = 200
	startY = 20
	message = request.Get.get('msg')
	response = ''
	resdir = []
	distance = 0	
	maxdis = 0      #最大的偏移量
	for i in message:
		#需要添加一个判断条件，判断是否查到了数据
		if u'\u4e00' <= i <= u'\u9fff':
			hanzi = Struts.objects.get(field_hanzi=i)
			if hanzi.struct == '00':
				response += '00'
				distance -= 2
			elif hanzi.struct == '01':
				response += '01'
			elif hanzi.struct == '10':
				response += '10'
			else:
				response += '11'
				distance += 2
			maxdis = max(maxdis, abs(distance))
	segment = (startX-50) // maxdis    #整除，取整数部分

	x = 0 
	x1 = startX  #上一个x,y的值
	y1 = startY
	for i in response:
		if i == '0':
			x -= 1
		else:
			x += 1
		x2 = startX+x*segment
		y2 = y1+startY
		d = 'M '+str(x1)+' '+str(y1)+' L '+str(x2)+' '+str(y2)
		resdir.append({'xs':x1, 'ys':y1, 'xe':startX+x*segment, 'ye':y2, 'd':d})
		x1 = startX+x*segment
		y1 = y2
		#resdir.append(startP+x*segment)
		print(resdir)
	return HttpResponse(json.dumps(resdir), content_type="application/json, charset=utf-8")
