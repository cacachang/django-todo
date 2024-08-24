from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    return render(request, "items/index.html", {"items": items})

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = Item(**form.cleaned_data)
            item.save()

            return redirect("items:index")
    return render(request, "items/new.html")


def update(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item.title = form.cleaned_data["title"]
            item.description = form.cleaned_data["description"]
            item.deadline = form.cleaned_data["deadline"]
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

