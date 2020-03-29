from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Struts
import json
def home(request):
	return render(request, "home.html")
def test(request):
	return render(request, "test.html")
def download1file(request):
	return render(request, "download1file.html")
def downloadAllfile(request):
	return render(request, "passages.html")
#吕浙青
def index(request):
    return render(request, "index.html")

def miaohong_home(request):
	return render(request, "home_miaohong.html")

def index2(request):
    return render(request, 'trans2.html')   #从templates的下一层目录开始写路径
def transform(request):
    dis = []
    startX = 500
    startY = 20
    message = request.GET.get('msg')
    response = ''
    for item in message:
        temp = Struts.objects.filter(field_hanzi=item)
        response += temp[0].struct

    x1 = startX  # 上一个x,y的值
    y1 = startY
    x=0
    count = 0
    for i in response:
        if i == '0':
            x = -1
        else:
            x = 1
        n = x * 150 + (-1) * x * count * 30
        x2 = x1 + n
        y2 = y1 + 3 * startY
        d = 'M ' + str(x1) + ' ' + str(y1) + ' L ' + str(x2) + ' ' + str(y2)
        dis.append({'xs': x1, 'ys': y1, 'xe': x1 + n, 'ye': y2, 'd': d, 'response':i})
        x1 = x2
        y1 = y2
        count += 1
    return HttpResponse(json.dumps(dis), content_type="application/json, charset=utf-8")
