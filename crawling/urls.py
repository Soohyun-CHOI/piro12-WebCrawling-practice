from django.urls import path

from crawling import views

urlpatterns = [
    path("", views.home, name="home")
]