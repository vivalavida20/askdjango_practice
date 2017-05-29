from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# x 또는 y값이 들어오지 않을 때 기본 값을 지
def mysum(request, numbers):

    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):

    return HttpResponse(
        "안녕하세요. {}입니다. 저는 {}살입니다.".format(name, age)
    )