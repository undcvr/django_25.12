from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
  
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
    

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')