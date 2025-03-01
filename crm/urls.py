from django.urls import path
from .views import LeadListView, LeadDetailView, SalesDashboardView

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('sales/dashboard/', SalesDashboardView.as_view(), name='sales-dashboard'),
]
