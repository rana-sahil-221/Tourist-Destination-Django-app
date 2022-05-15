from . import views
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('beach/',views.explore,name='explore'),
]
