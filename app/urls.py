from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get_main_menu', get_main_menu, name='get_main_menu'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('projects', projects, name='projects'),
    path('clients', clients, name='clients'),
    path('blogs', blogs, name='blogs'),
    path('careers', careers, name='careers'),
    path('contact', contact, name='contact'),
]