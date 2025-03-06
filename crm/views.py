import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from rest_framework.decorators import api_view

@api_view(['GET'])
def fetch_rea_leads(request):
  try:
    headers = {"Authorization": f"Bearer {settings.REA_API_KEY}"}
    response = requests.get(settings.REA_API_BASE_URL, headers=headers)
    
    if response.status_code == 200:
        leads_data = response.json()
        saved_leads = []
        for lead in leads_data:
            lead_obj, created = Lead.objects.update_or_create(
                phone=lead.get("phone"),
                defaults={
                    "customer_name": lead.get("name"),
                    "status": "new",
                },
            )
            saved_leads.append(
                {
                    "id": lead_obj.id,
                    "customer_name": lead_obj.customer_name,
                    "phone": lead_obj.phone,
                    "created": created,
                }
            )
        return Response(
            {"message": "Leads fetched successfully", "leads": saved_leads},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"error": "Failed to fetch leads", "details": response.text},
            status=response.status_code,
        )
  except Exception as e:
    return Response(
      {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )



@api_view(['POST'])
def fetch_flk_auth_token(request):
  url = f"{settings.FLK_API_BASE_URL}/oauth/token"
  payload = {
      'client_id': settings.FLK_CLIENT_ID,
      'client_secret': settings.FLK_CLIENT_SECRET,
      'grant_type': 'client_credentials',
  }
  response = requests.post(url, data=payload)
  if response.status_code == 200:
      token_data = response.json()
      return Response(token_data, status=status.HTTP_200_OK)
  else:
      return Response({"error": "Failed to authenticate", "details": response.text}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch_flk_leads(request):
  token = request.headers.get('Authorization')
  if not token:
    return Response({"error": "Authorization token is missing"}, status=status.HTTP_400_BAD_REQUEST)

  url = f"{settings.FLK_API_BASE_URL}/leads"
  headers = {
      'Authorization': f'Bearer {token}'
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
      leads = response.json()
      return Response(leads, status=status.HTTP_200_OK)
  else:
      return Response({"error": "Failed to fetch leads", "details": response.text}, status=status.HTTP_400_BAD_REQUEST)
