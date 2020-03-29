# -*- coding: UTF-8 -*-
from django.db import models
from HanziModel.models import ZywTHz 
from django.http import HttpResponse
import json

#该函数的功能是获取通过ajax传进来的字符串，拿到字符串后，对字符串做出来，转变成01代码
def transfer(request):	

	return HttpResponse(json.dumps(resdir), content_type="application/json, charset=utf-8")
