from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


# Takes a request and returns a response
def calculate():
    x = 1 
    y = 2
    return x


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Matthew'})
