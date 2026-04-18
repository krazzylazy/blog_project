from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Home'
    }
    return render(request, 'webroot/index.html', context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'webroot/about.html', context)

def contact(request):
    context = {
        'title' : 'Contact'
    }
    return render(request, 'webroot/contact.html', context)