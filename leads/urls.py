from django.urls import path
from .views import address_autocomplete, create_lead  # or any other views you have

urlpatterns = [
    path('create/', create_lead, name='create_lead'),
    path('address-autocomplete/', address_autocomplete, name='address_autocomplete'),
]
