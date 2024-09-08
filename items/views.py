from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponse
from django.template.loader import render_to_string
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()

    return render(request, "items/index.html", {'items': items})

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = Item(**form.cleaned_data)
            item.save()

            items = Item.objects.all()
            items_partial = render_to_string("items/_items.html", {'items': items})
            return HttpResponse(items_partial)
    return render(request, "items/new.html")


def update(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item.title = form.cleaned_data["title"]
            item.description = form.cleaned_data["description"]
            item.deadline = form.cleaned_data["deadline"]
            item.status = form.cleaned_data["status"]
            item.save()

            return redirect("items:index")
    else:
        form = ItemForm(item.__dict__)

    return render(request, "items/edit.html", {"form": form, "item": item})


def delete(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, id=id)

        item.delete()
        return redirect("items:index")
    else:
        return HttpResponseNotAllowed(["POST"])

