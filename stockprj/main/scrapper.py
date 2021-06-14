from django.shortcuts import render

def main(request):
    return render(request,'Scrapping/scrape.html')