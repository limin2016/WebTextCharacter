# -*- coding: UTF-8 -*-
from django.db import models
from HanziModel.models import ZywTHz, Passages
from django.http import HttpResponse
import json
from collections import deque

#该函数的功能是获取通过ajax传进来的字符串，拿到字符串后，对字符串做出来，转变成01代码
def transfer(request):	
	startX = 200
	startY = 20
	message = request.GET.get('msg')
	response = ''
	resdir = []
	distance = 0	
	maxdis = 0      #最大的偏移量                                                                                                                          
	for i in message:
		#需要添加一个判断条件，判断是否查到了数据
		if u'\u4e00' <= i <= u'\u9fff':
			hanzi = ZywTHz.objects.get(chinese=i)
			if hanzi.tone==0 or hanzi.tone==1 or hanzi.tone==3:
				response += '0'
				distance -= 1
			else:
				response +='1'
				distance += 1
			maxdis = max(maxdis, abs(distance))
	resdir.append({"code":response})
	return HttpResponse(json.dumps(resdir), content_type="application/json, charset=utf-8")

# def transfer(request):	
# 	startX = 200
# 	startY = 20
# 	message = request.GET.get('msg')
# 	response = ''
# 	resdir = []
# 	distance = 0	
# 	maxdis = 0      #最大的偏移量                                                                                                                          
# 	for i in message:
# 		#需要添加一个判断条件，判断是否查到了数据
# 		if u'\u4e00' <= i <= u'\u9fff':
# 			hanzi = ZywTHz.objects.get(chinese=i)
# 			if hanzi.tone%2==0:
# 				response += '0'
# 				distance -= 1
# 			else:
# 				response +='1'
# 				distance += 1
# 			maxdis = max(maxdis, abs(distance))
# 	segment = (startX-50) // maxdis

# 	x = 0 
# 	x1 = startX #上一个x，y的值
# 	y1 = startY
# 	for i in response:
# 		if i=='0':
# 			x -= 1
# 		else:
# 			x += 1==
# 		x2 = startX+x*segment
# 		y2 = y1+startY
# 		d = 'M '+str(x1)+' '+str(y1)+' L '+str(x2)+' '+str(y2)
# 		resdir.append({'xs':x1, 'ys':y1, 'xe':startX+x*segment, 'ye':y2, 'd':d})
# 		x1 = startX+x*segment
# 		y1 = y2
# 		#resdir.append(startP+x*segment)
# 	print(resdir)
# 	return HttpResponse(json.dumps(resdir), content_type="application/json, charset=utf-8")

def unifyPassage(request):
	response = [{"name":"二进制秘密消息：", "value1":"01", "sj":"-"},]
	for i in range(254): 
		passage = Passages.objects.get(id=i+1)
		data = {}
		data["name"] = str(i%2)
		data["path"] = passage.path
		data["passageName"] = passage.name
		response.append(data)
	q1 = deque([])
	q2 = deque([])
	q2.append("01")
	for i in range(127):
		temp = q2.popleft()
		q1.append(temp+"01")
		response[i*2+1]["value1"] = temp+"01"
		response[i*2+1]["sj"] = temp
		q2.append(temp+"01")

		q1.append(temp+"02")
		response[i*2+2]["value1"] = temp+"02"
		response[i*2+2]["sj"] = temp
		q2.append(temp+"02")
	print("执行一次")
	return HttpResponse(json.dumps(response), content_type="application/json, charset=utf-8")


