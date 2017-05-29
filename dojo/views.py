from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# x 또는 y값이 들어오지 않을 때 기본 값을 지정
def mysum(request, numbers):

    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)