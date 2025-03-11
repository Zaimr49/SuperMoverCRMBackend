from django.urls import path
from .views import fetch_flk_auth_token, fetch_flk_leads

urlpatterns = [
    
    # REA API ENDPOINTS
    # path('read/leads/', fetch_rea_leads, name='fetch-rea-leads'),

    # FLG API ENDPOINTS
    path('flk/token/', fetch_flk_auth_token, name='fetch-flk-auth-token'),
    path('flk/leads/', fetch_flk_leads, name='fetch-flk-leads'),

    
]
