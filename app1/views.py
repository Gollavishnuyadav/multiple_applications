from django.shortcuts import render

from django.http import HttpResponse

def a(request):
    return HttpResponse("a")

def b(request):
    return HttpResponse("b")