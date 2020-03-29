from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf



def search(request):
	arg = {}
	if request.POST:
		arg['rlt'] = request.POST['q']
	return render(request, 'search_form.html', arg)

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "search_post.html", ctx)