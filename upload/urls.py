from django.urls import path

from . import views

urlpatterns = [
    path("te/", views.te)
]
