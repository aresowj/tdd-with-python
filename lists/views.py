# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect(reverse('view_list'))

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
