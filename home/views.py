from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mul(request):
    if 'a' in request.GET and 'b' in request.GET:
        a = int(request.GET.get('a'))
        b = int(request.GET.get('b'))
        c = a * b

        context = {
            'a' : a, 
            'b' : b, 
            'c' : c
        }
        return render(request, 'mul.html', context)
    return HttpResponse("Bad Request")

def age(request, age):
    if 'name' in request.GET:
        context = {
            'age' : age,
            'name' : request.GET.get('name')
        }
        return render(request, 'age.html', context)
    return HttpResponse("Bas Request")

def fruits(request):
    fruits = ['Apple', 'Mango', 'Orange']
    context = {
        'fruits' : fruits
    }
    return render(request, 'fruits.html', context)