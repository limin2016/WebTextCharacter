from django.db import models
from BihuaModel.models import China
from django.http import HttpResponse
import json
import os
import io


def findtxt(root):
    file_names = os.listdir(root)
    file_ob_list = []
    for file_name in file_names:
        fileob = root + '/' + file_name
        file_ob_list.append(fileob)
    return file_ob_list


def readfile(filename):
    fileopen = io.open(filename, "r", encoding='utf-8-sig')
    for eachline in fileopen.readlines():
        texts = "".join(eachline)
    return texts


def transform(message):
    rr = ''
    resdir = []
    startX = 500
    startY = 20
    for i in message:
        if u'\u4e00' <= i <= u'\u9fff':
            zi = China.objects.get(cnword=i)
            if zi.bh % 2 == 0:
                rr += '0'
            else:
                rr += '1'
    m = 0
    x1 = startX
    y1 = startY
    for i in rr:
        if i == '0':
            x = -1
        else:
            x = 1
        n = x*110+(-1)*x*m*30
        x2 = x1+n
        y2 = y1+3*startY
        d = 'M '+str(x1)+' '+str(y1)+' L '+str(x2)+' '+str(y2)
        resdir.append({'xs': x1, 'ys': y1, 'xe': x1+n, 'ye': y2, 'd': d})
        x1 = x2
        y1 = y2
        m = m + 1
    return resdir


def tree(request):
    ret = []
    root = "/Users/wulimin/Desktop/WebTextCharacter/collection"
    lists = findtxt(root)
    for file in lists:
        texts = readfile(file)
        resdir = transform(texts)
        ret += resdir
    return HttpResponse(json.dumps(ret), content_type="application/json, charset=utf-8")
