# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    lst = List.objects.prefetch_related('item_set').get(id=list_id)
    return render(request, 'list.html', {'list': lst})


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = mark_safe("You can't have an empty list item")
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % list_.id)


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list_id=list_id)
    return redirect('/lists/%d/' % list_.id)
