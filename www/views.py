from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, 'www/frontpage.html')

def board(request):
    return render(request, 'www/frontpage.html')

def concept(request):
    return render(request, 'www/frontpage.html')

def gallery(request):
    return render(request, 'www/frontpage.html')

def publications(request):
    return render(request, 'www/frontpage.html')

def faq(request):
    return render(request, 'www/frontpage.html')

def links(request):
    return render(request, 'www/frontpage.html')

def map(request):
    return render(request, 'www/frontpage.html')

def feedback(request):
    return render(request, 'www/frontpage.html')