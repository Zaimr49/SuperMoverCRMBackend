from django.urls import path
from .views import fetch_flk_auth_token, fetch_flk_leads_from_db, fetch_flk_leads_from_api, save_lead, \
    address_autocomplete

urlpatterns = [
    
    # REA API ENDPOINTS
    # path('read/leads/', fetch_rea_leads, name='fetch-rea-leads'),

    # FLG API ENDPOINTS
    path('flk/token/', fetch_flk_auth_token, name='fetch-flk-auth-token'),
    path('flk/leads-api/', fetch_flk_leads_from_api, name='fetch-flk-leads-api'),
    path('flk/leads-db/', fetch_flk_leads_from_db, name='fetch-flk-leads-db'),
    path("flk/save-lead/", save_lead, name="save_lead"), 
    
    path('address-autocomplete/', address_autocomplete, name='address_autocomplete'),
    
]
