from django.urls import path

from rest_api import views

urlpatterns = [
    path('hello/', views.HelloWorld.as_view())
]