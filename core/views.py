from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from courses.models import Course
from django.db.models import Count


def home(request):
    top_courses = Course.objects.annotate(
        enrollment_count=Count("enrollment")
    ).order_by("-enrollment_count")[:3]
    return render(request, "core/index.html", context={"top_courses": top_courses})


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("core:home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "core/login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "Passwords do not match")
        else:
            user = User.objects.filter(username=username).first()
            if user:
                messages.error(request, "User with this username already exists")
            else:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                messages.success(request, "User Created Successfully")
                return redirect("core:login")
    return render(request, "core/register.html")


def logout(request):
    auth_logout(request)
    return redirect("core:home")
