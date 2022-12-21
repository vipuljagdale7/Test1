"""Fruit_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from fruitapp.views import homepage, show_fruits ,edit_fruit,delete_fruit,soft_delete,not_available_fruit,available_fruit
from fruitapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name="home"),
    path('show-fruits/', show_fruits, name="show_fruits"),  
    path('edit-fruit/<int:pk>/', edit_fruit, name="edit_fruit"),
    path('delete-fruits/<int:pk>/', delete_fruit,name="delete_fruit"),  
    path('soft-delete/<int:pk>/', soft_delete ,name="soft_delete"),
    path('available-fruit/', available_fruit ,name="available_fruit"),
    path('not-available-fruit/', not_available_fruit ,name="not_available_fruit"),


    # class based view
    # path('cbv-home/', views.Home.as_view(), name='home')

]










