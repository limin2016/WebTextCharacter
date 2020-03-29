# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from myapp.models import Struts

tmp = []


class Text(object):
    def __init__(self, url, content):
        self.url = url
        self.content = content

    def print_text(self):
        print('%s:%s' % (self.url, self.content))

    def print_content(self):
        return self.content


def findtxt(path, ret):
    filelist = os.listdir(path)
    for filename in filelist:
        de_path = os.path.join(path, filename)
        if os.path.isfile(de_path):
            if de_path.endswith(".txt"): #Specify to find the txt file.
                ret.append(de_path)
        else:
            findtxt(de_path, ret)


def readtxt(path):
    myfile = open(path, "r", encoding='UTF-8-sig')
    for eachline in myfile.readlines():
        # 去掉文本中的空格 数字等
        lines = filter(lambda
                           ch: ch not in ' 1234567890（）.%-=——+*&……￥#@！~·qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM“”，‘’：【】{}？。、；',
                       eachline)
        new_lines = list(lines)
        new_str = "".join(new_lines)
    return new_str


def ww(request):
    ret = []
    dis = []
    root = "/Users/wulimin/Desktop/WebTextCharacter/txt"
    findtxt(root, ret)
    for path in ret:
        print(path)
        string = readtxt(path)
        response1 = ''
        for var in string:
            temp = Struts.objects.filter(field_hanzi=var)
            response1 += temp[0].struct
        startX = 500
        startY = 20
        x = 0
        segment = 100
        # x1 = startX  # 上一个x,y的值
        # y1 = startY
        # pianyi = x1/2
        # if response1[0] == 0:
        #     x2 = pianyi
        # else:
        #     x2 = x1 + pianyi
        # for i in response1:
        #     if i == 0:
        #         if x2 > startX:
        #             pianyi = (x1-startX-15)/2
        #             x2 = x1-pianyi
        #         else:
        #             pianyi = (x1 - 15) / 2
        #             x2 = pianyi
        #     else:
        #         if x2 > startX:
        #             pianyi = (x2 - startX - 15) / 2
        #             x2 = x1*2 + pianyi
        #         else:
        #             pianyi = (x1-15)/2
        #             x2 = x1*2 - pianyi
        #     y2 = y1 + startY
        #     d = 'M ' + str(x1) + ' ' + str(y1) + ' L ' + str(x2) + ' ' + str(y2)
        #     dis.append({'xs': x1, 'ys': y1, 'xe': x2, 'ye': y2, 'd': d})
        #     x1 = x2
        #     y1 = y2
        # for i in response1:
        #     if i == '0':
        #         x = x - 1
        #     else:
        #         x = x + 1
        #     x2 = startX + x * segment
        #     y2 = y1 + startY
        #     d = 'M ' + str(x1) + ' ' + str(y1) + ' L ' + str(x2) + ' ' + str(y2)
        #     dis.append({'xs': x1, 'ys': y1, 'xe': x2, 'ye': y2, 'd': d})
        #     compareX.append(x1)
        #     x1 = startX + x * segment
        #     y1 = y2
        count = 0
        x1 = startX
        y1 = startY
        for i in response1:
            if i == '0':
                x = -1
            else:
                x = 1
            n = x * 150 + (-1) * x * count * 30
            x2 = x1 + n
            y2 = y1 + 3 * startY
            d = 'M ' + str(x1) + ' ' + str(y1) + ' L ' + str(x2) + ' ' + str(y2)
            dis.append({'xs': x1, 'ys': y1, 'xe': x1 + n, 'ye': y2, 'd': d})
            x1 = x2
            y1 = y2
            count += 1
    return HttpResponse(json.dumps(dis), content_type="application/json, charset=utf-8")

