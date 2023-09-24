from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request,"index.html")
def Tshirt(request):
    return render(request,"Tshirt.html")
def profile(request):
    return render(request,"profile.html")
