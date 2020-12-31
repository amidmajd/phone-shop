from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    return render(request, 'basket.html')


@login_required
def addphone(request):
    return redirect('basket:home')


@login_required
def removephone(request):
    return redirect('basket:home')
