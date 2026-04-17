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