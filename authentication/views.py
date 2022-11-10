from django.http.request import HttpRequest
from django.shortcuts import redirect, render 
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from django.contrib.auth.models import User
from django.contrib import messages 
from django.urls import reverse


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(reverse("shortener:index"))

    if request.method == "POST":
        if request.POST['email'] and request.POST['password']:
            user = authenticate(username=request.POST["email"], password=request.POST["password"])
            if user is not None:
                user_login(request, user)
                return redirect(reverse("shortener:index"))
            return render(request, "authentication/login.html", {"error": "invalid credentials"})
        return render(request, "authentication/login.html", {"error": "Empty fields"})

    return render(request, "authentication/login.html")


def logout(request):
    user_logout(request)
    return redirect(reverse("shortener:index"))


def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(reverse("shortener:index"))

    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if email and username and password:
            if password == request.POST.get("password2"):
                if User.objects.filter(email=email).exists() or User.objects.filter(username=username):
                    return render(request, "authentication/register.html", {"error": "User already exists"})
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, "Account created, please login")
                    return redirect(reverse("authentication:login"))
            return render(request, "authentication/register.html", {"error": "Passwords don't match"})
        return render(request, "authentication/register.html", {"error": "Please fill all fields"})

    return render(request, "authentication/register.html")


