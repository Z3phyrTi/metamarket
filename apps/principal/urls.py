from django.urls import path
from .views import principal
urlpatterns = [
    path('',principal, name='principal'),
]