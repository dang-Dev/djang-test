from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name="home"),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]