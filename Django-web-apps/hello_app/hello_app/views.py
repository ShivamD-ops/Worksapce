from django.http import HttpResponse
from .models import PersonModel
from .forms import PersonForm
from django.shortcuts import render

def hello_world(req):
    return HttpResponse("Welcome to Django Shivam")

def create_view(req):
    context = {}
    form = PersonForm(req.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(req,"create_view.html",context)