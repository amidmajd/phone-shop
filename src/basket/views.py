from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from basket.models import Basket
from phones.models import Phone


@login_required
def home(request):
    items = list(Basket.objects.filter(user=request.user).order_by("add_datetime"))

    if request.method == 'POST':
        for item in items:
            item.count = int(request.POST.get(item.phone.id))
            if item.count <= 0:
                item.delete()       # deleting from database
                items.remove(item)  # deleting from items list
            else:
                item.save()

    context = {
        'basket_items': items,
        'items_count': len(items),
        'total_price': sum([item.phone.price * item.count for item in items])
    }

    return render(request, 'basket.html', context=context)


@login_required
def addphone(request, phone_id):
    temp_item = Basket.objects.filter(user=request.user, phone=phone_id)

    if temp_item:   # adding to counter if item already in basket
        temp_item = temp_item.get()
        temp_item.count += 1
        temp_item.save()
    else:
        Basket.objects.create(user=request.user, phone=Phone.objects.get(id=phone_id))

    return redirect('basket:home')


@login_required
def removephone(request, phone_id):
    get_object_or_404(Basket, user=request.user, phone=phone_id).delete()
    return redirect('basket:home')
