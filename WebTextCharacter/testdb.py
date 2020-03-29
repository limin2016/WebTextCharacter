from django.http import HttpResponse, FileResponse
from HanziModel.models import Passages 
from django.shortcuts import render
import json
from django.db import models
from django.http import HttpResponse
from people.models import PeopleHanzidb



def insertPassages(request):	
	for i in range(254):
		passages = Passages(id=i+1, name="文章 copy "+str(i+1), path="/Users/wulimin/Desktop/WebTextCharacter/passages/文章copy"+str(i+1))
		passages.save()
	return HttpResponse('数据添加成功')

def downloadFile(request):
	filename = str(request.GET.get('filename'))+".txt"
	#filename = '你好.txt'.encode('utf-8')
	file = open("passages/"+filename,"rb")
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	#response['Content-Disposition'] = 'attachment;filename="{0}"'.format(name.encode('utf8').decode('ISO-8859-1'))
	response['Content-Disposition'] = 'attachment;filename=%s' % filename.encode('utf8').decode('ISO-8859-1')
	return response

# def showDownloadFile(request):
# 	response = {}
# 	data = []
# 	for i in range(254):
# 		passage = Passages.objects.get(id=i+1)
# 		data.append(passage.name)
# 	response["files"] = data
# 	return render(response, "passages.html", response)

def getFileName(request):
	response = []
	for i in range(254):
		passage = Passages.objects.get(id=i+1)
		response.append({"filename":passage.name, "href":"/download-file?filename="+passage.name})
	return HttpResponse(json.dumps(response), content_type="application/json, charset=utf-8")

#吕浙青
def testdb(request):
    startX = 500
    startY = 20
    #High = 3 * 3
    High = 4
    segment0 = pow(2, High) * 3 / 2  # 初始偏移量
    resdir = []
    Str = ""
    essay = request.GET.get('msg')

    for i in essay:
        if u'\u4e00' <= i <= u'\u9fff':
            test1 = PeopleHanzidb.objects.get(chinese=i)
            Str += test1.code
    print(Str)
    count = 0
    x1 = startX  # 上一个x，y的值
    y1 = startY
    segmentX = segment0
    segmentY = 100
    for i in Str:
        if i == '0':
            x = -1
        else:
            x = 1
        x2 = x1 + x * segmentX
        y2 = y1 + segmentY
        d = 'M ' + str(x1) + ' ' + str(y1) + ' L ' + str(x2) + ' ' + str(y2)
        resdir.append({'xs': x1, 'ys': y1, 'xe': x2, 'ye': y2, 'd': d})
        x1 = x2
        y1 = y2
        segmentX = segmentX/2
        count += 1
        if count % High == 0:
            x1 = startX
            y1 = startY
            segmentX = segment0
            print(count, ',')
    # print(Str)
    # return render(request, "index.html", {"resdir": resdir})
    return HttpResponse(json.dumps(resdir), content_type="application/json, charset=utf-8")


