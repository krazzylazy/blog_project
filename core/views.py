from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About this function")

# def hello(request):
#     return HttpResponse("Hello")

def hello(request, name):
    return HttpResponse(f"Hello {name}")

def add(request, num1, num2):
    return HttpResponse(f"Addition of {num1} and {num2} is {num1 + num2}")

def mul(request):
    if 'num1' in request.GET and 'num2' in request.GET:
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        return HttpResponse(f"Multiplication of {num1} and {num2} is {int(num1) * int(num2)}")
    return HttpResponse("Multiplication: No query parameters")