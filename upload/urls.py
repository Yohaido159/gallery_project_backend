from django.contrib import admin
from django.urls import path, include, re_path

from .views import GenerateRandomUserView

urlpatterns = [
    path("", GenerateRandomUserView.as_view(), name="home"),
]
