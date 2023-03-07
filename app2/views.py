from django.shortcuts import render

from django.http import HttpResponse

def c(request):
    return HttpResponse("c")

def d(request):
    return HttpResponse("d")