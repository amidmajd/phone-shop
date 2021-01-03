from django.shortcuts import render
from django.core.paginator import Paginator
from phones.models import Phone


def home(request):
    latest_5_phones = Phone.objects.all().order_by('-add_datetime')[:5]
    return render(request, 'home.html', {"phones": latest_5_phones})


def shop(request):
    phones = Phone.objects.all().order_by('-add_datetime')

    paginator = Paginator(phones, 6)    # Show X phones per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop.html', {"phones_page_obj": page_obj})


def contactus(request):
    return render(request, 'contactus.html')
