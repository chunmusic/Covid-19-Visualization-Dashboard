from django.contrib import admin
from django.urls import path
from .views import dashboardview

urlpatterns = [
    path('', dashboardview),
]
