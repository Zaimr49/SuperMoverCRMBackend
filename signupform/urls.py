from django.urls import path
from .views import create_signup

urlpatterns = [
    path('create/', create_signup, name='create_signup'),
]
