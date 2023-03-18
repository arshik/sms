from django.shortcuts import render

def frontend(request):
    return render(request,"frontend.html")

def backend(request):
    return render(request,"backend.html")