'''from django.urls import path
from .views import greet_api

urlpatterns = [
    path('api/greet/', greet_api, name='greet-api'),
]'''
from django.urls import path
from .views import greet_api

urlpatterns = [
    path('api/greet/', greet_api.as_view(), name='greet'),
]