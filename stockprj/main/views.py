from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def aboutus(request):
    return render(request,'about.html')

def news(request):

    
    return render(request,'news.html')

def costcal(request):
    return render(request,'tools/costcalc.html')