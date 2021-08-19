from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("insert", views.insert, name="Insert"),
    path("showdata", views.showdata, name="Showdata"),
    path("update", views.update, name="Update"),
    path("updated", views.updated, name="Updated"),
]
