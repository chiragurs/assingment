from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    return HttpResponse("<h1>Your project is ready to be started..<h1>")

def base(request):
    return render(request,"base.html")

def collection(request):
    return render(request,"myapp/collection.html")

def home(request):
    return render(request,"myapp/home.html")

