from django.urls import path
from .views import login, logout, register

app_name = "authentication"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
