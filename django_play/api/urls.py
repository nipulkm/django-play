
from importlib.resources import path
from unicodedata import name

from django.urls import path
from .views import PlayViewApi

urlpatterns = [
    path('play', PlayViewApi.as_view(), name='play_view_api'),
]