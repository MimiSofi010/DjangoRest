from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayQuote(request):
    return HttpResponse("<h2> The best investment we can do is in ourself </h2>")
