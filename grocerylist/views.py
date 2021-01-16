from django.shortcuts import render, reverse, get_object_or_404
from .models import Groceries
from django.http import HttpResponseRedirect
from django.utils import timezone


def index(request):
    items = Groceries.objects.all()

    context = {
        'items': items
    }
    return render(request, 'grocerylist/index.html', context)


def complete(request):
    items = Groceries.objects.all()

    context = {
        'items': items
    }
    return render(request, 'grocerylist/complete.html', context)


def create_todo(request):
    # get the form data out of request.POST
    description = request.POST['description']
    # create an instance of our model
    todo_item = Groceries(description=description, createdate=timezone.now())
    # save a new record to the database
    todo_item.save()
    # redirect the the index page
    return HttpResponseRedirect(reverse('grocerylist:index'))


def complete_todo(request, item_id):
    item = get_object_or_404(Groceries, pk=item_id)
    item.completedate = timezone.now()
    item.completed = True
    item.save()

    return HttpResponseRedirect(reverse('grocerylist:index'))
