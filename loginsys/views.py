from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import AdventureRecords
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
import string

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
    if request.method == "POST":
        username = request.POST["username"]
        raw_password = request.POST["password_1"]
        pw_confirm = request.POST["password_2"]
        email = request.POST["email"]
        allowed_char = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@.+-_'
        if not username or not raw_password or not pw_confirm or not email:
            error_m = "Fill all the blank please."
        elif raw_password != pw_confirm:
            error_m = "Password confirmation fail."
        elif User.objects.get(username=username):
            error_m = "Username already exist."
        elif User.objects.get(email=email):
            error_m = "E-mail already exist."
        elif len(username) < 5 or len(raw_password) < 8:
            error_m = "Username or password too short."
        # https://stackoverflow.com/questions/1323364
        elif not all(c in allowed_char for c in username):
            error_m = "Username not allowed."
        elif not all(c in allowed_char for c in raw_password):
            error_m = "Password invalid."
        elif not all(c in allowed_char for c in email):
            error_m = "E-mail invalid."
        elif not email.count('@') == 1:
            error_m = "E-mail invalid."
        else:
            # checking pass
            # TODO create user after debug
            error_m = "Your username is [" + username + "] and password is [" + raw_password + "] and e-mail is [" + email + "]"
        # error appears
        return render(request, "loginsys/register_form.html", {"message": error_m})

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    else:
        return render(request, "loginsys/register_form.html")