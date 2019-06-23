from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import AdventureRecords
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "loginsys/login_page.html")
    context = {
        "adRec": AdventureRecords.objects.get(holder_id=request.user)
    }
    # no html
    # return HttpResponse("Hello, test.")
    return render(request, "loginsys/home.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('homepage'))
    else:
        return render(request, "loginsys/login_page.html", {"message": "No user found."})

def logout_view(request):
    logout(request)
    return render(request, "loginsys/login_page.html", {"message": "Logout."})

def register_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    else:
        context = {
            "form": UserCreationForm(),
        }
        return render(request, "loginsys/register_form.html", context)