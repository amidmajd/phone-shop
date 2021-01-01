from django.shortcuts import render
from phones.models import Phone


def home(request):
    latest_5_phones = Phone.objects.all().order_by('-add_datetime')[:5]
    return render(request, 'home.html', {"phones": latest_5_phones})


def shop(request):
    objs = Phone.objects.all().order_by('-add_datetime')
    return render(request, 'shop.html', {"phones": objs})


def contactus(request):
    return render(request, 'contactus.html')
