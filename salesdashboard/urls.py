# salesdashboard/urls.py
from django.urls import path
from .views import (
    new_leads,
    in_progress_leads,
    lead_source,
    retailers,
    commission_tracking,
    financial_reconciliation,
)

urlpatterns = [
    path('new-leads/', new_leads, name='new_leads'),
    path('in-progress-leads/', in_progress_leads, name='in_progress_leads'),
    path('lead-source/', lead_source, name='lead_source'),
    path('retailers/', retailers, name='retailers'),
    path('commission-tracking/', commission_tracking, name='commission_tracking'),
    path('financial-reconciliation/', financial_reconciliation, name='financial_reconciliation'),
]
