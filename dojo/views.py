import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
# x 또는 y값이 들어오지 않을 때 기본 값을 지
def mysum(request, numbers):

    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):

    return HttpResponse(
        "안녕하세요. {}입니다. 저는 {}살입니다.".format(name, age)
    )

def post_list1(request):
    name = '공유'

    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>템플릿 테스트</p>
    '''.format(name=name))

def post_list2(request):
    name = '공유'

    return render(request, 'dojo/post_list.html', {'name':name})

def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '안녕', '장고'],
    }, json_dumps_params={'ensure_ascii' : False})ç

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'studymember.xlsx')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response