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

""" 
@api_view(['GET'])
def address_autocomplete(request):
   
    query = request.GET.get('query', '')
    if not query:
        return Response([], status=status.HTTP_200_OK)

    nominatim_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": query,
        "format": "json",
        "addressdetails": 1,  # Set to 1 to get more details in 'address'
        "limit": 5,
        "countrycodes": "au"  # restrict to Australia, if desired
    }
    headers = {
        "User-Agent": "SuperMoverCRM/1.0 (zaeemr49@gmail.com)"
    }

    response = requests.get(nominatim_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Instead of returning just the display_name (string),
        # return an object with both display_name and address.
        suggestions = []
        for item in data:
            suggestions.append({
                "display_name": item.get("display_name", ""),
                "address": item.get("address", {})
            })
        return Response(suggestions, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Failed to fetch suggestions"}, status=response.status_code)
 """