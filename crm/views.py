import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import Flk_lead
from rest_framework.decorators import api_view
from .utils import get_flk_access_token
from datetime import datetime

@api_view(['POST'])
def fetch_flk_auth_token(request):
    access_token = get_flk_access_token()
    return Response({
        "access_token": access_token
    })

@api_view(['GET'])
def fetch_flk_leads(request):
    params = {"submitted": "2025-03-09T00:00:00Z"}  # Modify as needed
    # submitted_date = datetime(2025, 3, 9).isoformat() + "Z"
    # params = {"submitted": submitted_date}
    url = f"{settings.FLK_API_BASE_URL}/leads"
    access_token = get_flk_access_token()
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("** Error:", response.text)
        return Response({
            "error": response.text
        })
    leads = response.json()  # Assuming response is a list of leads
    created_leads = []
    for lead in leads:
        # Extract required fields
        customer_name = f"{lead['tenant']['firstName']} {lead['tenant']['secondName']}"
        phone = lead['tenant']['mobile']
        lead_obj, created = Flk_lead.objects.update_or_create(
            phone=phone,  # Assuming phone is unique
            defaults={
                "customer_name": customer_name,
                "tenant": lead.get("tenant", {}),
                "address": lead.get("address", {}),
                "referring_agent": lead.get("referringAgent", {}),
                "referring_agency": lead.get("referringAgency", {}),
                "services": lead.get("services", {}),
                "submitted": lead.get("submitted"),
                "lease_start_date": lead.get("leaseStartDate"),
                "renewal": lead.get("renewal", False),
            }
        )
        if created:
            created_leads.append(lead_obj.customer_name)
    return Response({"message": "Leads stored successfully", "created_leads": created_leads})
        

