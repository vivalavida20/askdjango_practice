from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# x 또는 y값이 들어오지 않을 때 기본 값을 지정
def mysum(request, x=0, y=0, z=0):
    # request : HttpRequest
    return HttpResponse(int(x) + int(y))