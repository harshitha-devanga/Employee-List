from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('',views.about,name='about'),
    path('add/<int:a>/<int:b>',views.add)
]