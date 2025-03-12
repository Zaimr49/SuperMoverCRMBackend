from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import LeadSerializer
import requests
from django.conf import settings

@api_view(['POST'])
def create_lead(request):
    """
    Creates a new Lead from the JSON data sent by the frontend.
    """
    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def address_autocomplete(request):
#     """
#     Return a list of possible addresses based on the 'query' GET parameter
#     using the Google Places API.
#     """
#     query = request.GET.get('query', '')
#     if not query:
#         return Response([], status=status.HTTP_200_OK)

#     google_api_key = settings.GOOGLE_API_KEY  # Ensure this key is set in your settings
#     google_api_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"

#     # Prepare parameters. You can also include additional parameters like `types` or `components`.
#     params = {
#         "input": query,
#         "key": google_api_key,
#         "types": "address",
#         # "components": "country:au",  # Uncomment and adjust for country restrictions, e.g., Australia.
#     }

#     response = requests.get(google_api_url, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         # Parse the JSON response to extract the address suggestions.
#         suggestions = [prediction['description'] for prediction in data.get('predictions', [])]
#         return Response(suggestions, status=status.HTTP_200_OK)
#     else:
#         return Response({"error": "Failed to fetch suggestions"}, status=response.status_code)

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
