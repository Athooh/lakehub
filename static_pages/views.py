from django.shortcuts import  render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def shop(request):
    return render(request, 'pages/shop.html') 

def help(request):
    return render(request, 'pages/help.html') 

def about(request):
    return render(request, 'pages/about.html') 

def services(request):
    return render(request, 'pages/service.html') 

def contact(request):
    return render(request, 'pages/contact.html') 