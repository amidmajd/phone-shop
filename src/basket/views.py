from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'basket.html')


def addphone(request):
    return redirect('basket:home')


def removephone(request):
    return redirect('basket:home')
