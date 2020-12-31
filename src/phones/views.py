from django.shortcuts import render
from django.shortcuts import get_object_or_404, Http404
from phones.models import Phone


def phonedetail(request, id):
    instance = get_object_or_404(Phone, id=id)
    return render(request, 'phonedetail.html', {"instance": instance})
