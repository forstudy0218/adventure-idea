from django.http import HttpResponse
from django.shortcuts import render
from .models import AdventureRecords

# Create your views here.
def index(request):
    context = {
        "adRec": AdventureRecords.objects.all()
    }
    # no html
    # return HttpResponse("Hello, test.")
    return render(request, "loginsys/home.html", context)