from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
# from django.db.models import Q
from phones.models import Phone


def home(request):
    latest_5_phones = Phone.objects.all().order_by('-add_datetime')[:5]
    return render(request, 'home.html', {"phones": latest_5_phones})


def shop(request):
    brand_choices = [brand[1] for brand in Phone.brand.field.choices]

    if request.GET.get('filter'):  # if filter button is pressed
        brands = [brand for brand in brand_choices if request.GET.get('b-' + brand)]
        if not brands:  # checking if brands is empty then ignore brands filter
            brands = brand_choices.copy()

        # checking if price_range is valid and set, otherwise ignore price filter by using max numbers
        try:
            price_range = (int(request.GET.get('price_from')), int(request.GET.get('price_to')))
        except:
            price_range = (0, 9223372036854775807)

        phones = Phone.objects.filter(
            brand__in=brands,
            price__range=price_range
        ).order_by('-add_datetime')

    elif request.GET.get('search'):  # if search button is pressed
        search_query = request.GET.get('search_query')

        # with postgresSQL
        phones = Phone.objects.annotate(
            search=SearchVector('name', 'brand')
        ).filter(
            search=search_query
        ).order_by('-add_datetime')

        # # without postgresSQL
        # phones = Phone.objects.filter(
        #     Q(name__contains=search_query) | Q(brand__contains=search_query)
        # ).order_by('-add_datetime')

    else:   # default output
        phones = Phone.objects.all().order_by('-add_datetime')

    paginator = Paginator(phones, 6)    # Show X phones per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop.html', {"phones_page_obj": page_obj, 'brand_choices': brand_choices})


def contactus(request):
    return render(request, 'contactus.html')
