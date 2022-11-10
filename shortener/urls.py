from django.urls import path
from .views import DashboardView, DeleteView, RedirectView, ShortenView 

app_name = "shortener"

urlpatterns = [
    path('', ShortenView.as_view(), name="index"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('delete/', DeleteView.as_view(), name="delete"),
    path('<str:short>/', RedirectView.as_view(), name="redirect"),
]