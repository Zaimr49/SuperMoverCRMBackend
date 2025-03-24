import requests
from rest_framework.response import Response
from .models import Flk_lead
from rest_framework.decorators import api_view
from .utils import get_flk_access_token
from datetime import datetime
from django.http import JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from .serializer import FlkLeadSerializer
from django.db.models import Q
import logging
from rest_framework import status


@api_view(['POST'])
def fetch_flk_auth_token(request):
    access_token = get_flk_access_token()
    return Response({
        "access_token": access_token
    })

@api_view(['GET'])
def fetch_flk_leads_from_api(request):
    
    params = {"submitted": "2025-03-09T00:00:00Z"}  # Modify as needed
    submitted_date = request.GET.get("submitted")
    if not submitted_date:
        return JsonResponse({"error": "Missing required parameter: submitted"}, status=400)

    # submitted_date = datetime(2025, 3, 9).isoformat() + "Z"
    params = {"submitted": submitted_date}
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
                "extra": lead.get("extra", {}),
                "submitted": lead.get("submitted"),
                "lease_start_date": lead.get("leaseStartDate"),
                "renewal": lead.get("renewal", False),
            }
        )
        if created:
            created_leads.append(lead_obj.customer_name)
    return Response({"message": "Leads stored successfully", "created_leads": created_leads})

def get_flk_leads_from_db(page_number=1, status="New", items_per_page=5, filter_date=None):
    query = Q()
    if filter_date:
        filter_date = datetime.strptime(filter_date, "%Y-%m-%d")
        query &= Q(submitted__gte=filter_date)
    if status:
        query &= Q(
            status=status.lower()
        )
    leads_queryset = Flk_lead.objects.filter(query)
    paginator = Paginator(leads_queryset, items_per_page)  # Paginate the queryset
    page = paginator.get_page(page_number)
    has_more_data = page.has_next()
    leads = []
    for lead in page:
        d = lead.__dict__
        del d['_state']
        leads.append(d)
    return {
        'leads': leads,  # List of leads in the current page
        'next_page': page.next_page_number() if has_more_data else None,
        'hasMoreData': has_more_data,
        'totalPages': paginator.num_pages
    }

@api_view(['GET'])
def fetch_flk_leads_from_db(request):
    try:
        page = int(request.GET.get("page"))
    except:
        page = 1
    status = request.GET.get("status")
    leads_ = get_flk_leads_from_db(page_number=page, status=status)
    return Response(leads_)


# logger = logging.getLogger(__name__)

@api_view(['POST'])
def save_lead(request):
    try:
        data = request.data

        # ✅ Ensure data is a dictionary
        if isinstance(data, list):
            data = data[0]  # Extract first object if it's a list

        data = dict(data)  # Ensure mutability

        # Extract tenant details
        tenant = data.get("tenant", {})

        # ✅ Assign defaults if missing
        data.setdefault("customer_name", f"{tenant.get('firstName', '')} {tenant.get('secondName', '')}".strip())
        data.setdefault("phone", tenant.get("mobile", ""))
        data.setdefault("referring_agent", {})
        data.setdefault("referring_agency", {})
        data.setdefault("lease_start_date", None)
        data.setdefault("extra", {}) 

        is_sale = data["extra"].get("sale", False)

        # logger.info(f"Processed lead data: {data}")

        # ✅ Validate and save data
        serializer = FlkLeadSerializer(data=data)
        if serializer.is_valid():
            lead_obj, created = Flk_lead.objects.update_or_create(
                phone=serializer.validated_data.get("phone", ""),
                defaults={**serializer.validated_data, "status": "sale" if is_sale else "new"}
            )

            response_serializer = FlkLeadSerializer(lead_obj)
            return Response({"done": True, "data": response_serializer.data}, status=status.HTTP_201_CREATED)

        # logger.warning(f"Validation failed: {serializer.errors}")
        return Response({"done": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        # logger.error(f"Error in save_lead: {str(e)}", exc_info=True)
        return Response({"done": False, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def address_autocomplete(request):
    """
    Return a list of possible addresses based on the 'query' GET parameter
    using OpenStreetMap's Nominatim API, including detailed address info.
    """
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
