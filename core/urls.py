from django.urls import path
from .views import home, about, contact, login, register, logout

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
]
