from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def new_leads(request):
    """Return mock data for New Leads (last month and current month)."""
    data = [
        {"name": "Last month", "value": 60},
        {"name": "Current month", "value": 80},
    ]
    return Response(data)

@api_view(['GET'])
def in_progress_leads(request):
    """Return mock data for In-Progress Leads."""
    data = [
        {"name": "Last month", "value": 70},
        {"name": "Current month", "value": 50},
    ]
    return Response(data)

@api_view(['GET'])
def lead_source(request):
    """Return mock data for Sales by Lead Source."""
    data = [
        {"name": "REA office", "value": 50},
        {"name": "REA software", "value": 70},
    ]
    return Response(data)

@api_view(['GET'])
def retailers(request):
    """Return mock data for Sales Product by Retailers."""
    data = [
        {"name": "Electricity", "value": 40},
        {"name": "Gas", "value": 70},
        {"name": "Dual Fuel", "value": 50},
    ]
    return Response(data)

@api_view(['GET'])
def commission_tracking(request):
    """Return mock data for Commission Tracking."""
    data = {
        "pending": 10,
        "confirmed": 5,
        "message": "Commission tracking details",
    }
    return Response(data)

@api_view(['GET'])
def financial_reconciliation(request):
    """Return mock data for Financial Reconciliation Reports."""
    data = {
        "reports": [
            {"report": "Leads Received", "count": 100},
            {"report": "Sales Processed", "count": 80},
            {"report": "Product Names", "count": 5},
            {"report": "Customer Details", "count": 120},
            {"report": "Retailer Details", "count": 3},
            {"report": "Transaction Dates", "count": 20},
        ]
    }
    return Response(data)
