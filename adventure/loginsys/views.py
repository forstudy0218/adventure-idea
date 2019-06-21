from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # no html
    return HttpResponse("Hello, test.")