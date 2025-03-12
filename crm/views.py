import requests
from rest_framework.response import Response
from .models import Flk_lead
from rest_framework.decorators import api_view
from .utils import get_flk_access_token
from datetime import datetime
from django.http import JsonResponse
from django.conf import settings
from django.core.paginator import Paginator

@api_view(['POST'])
def fetch_flk_auth_token(request):
    access_token = get_flk_access_token()
    return Response({
        "access_token": access_token
    })

@api_view(['GET'])
def fetch_flk_leads_from_api(request):
    # params = {"submitted": "2025-03-09T00:00:00Z"}  # Modify as needed
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
#     leads = [
#   {
#     "tenant": {
#       "firstName": "Maria",
#       "secondName": "Morgan",
#       "email": "cbrown@example.net",
#       "mobile": "+1-366-745-0412"
#     },
#     "address": {
#       "text": "86304 Heather Fields Suite 989\nPort Tomtown, MN 22733",
#       "unit": "17",
#       "streetNumber": "12",
#       "streetName": "Patton Plain",
#       "locality": "Sharonview",
#       "postCode": 4995,
#       "state": "Wisconsin",
#       "city": "South Yvonne",
#       "country": "Western Sahara"
#     },
#     "referringAgent": {
#       "name": "Charlotte Johnson",
#       "email": "anthony34@example.com",
#       "partnerCode": "12db89c7-c3a4-4f79-bbd7-26c2cab929d7"
#     },
#     "referringAgency": {
#       "name": "Wilson LLC",
#       "email": "qmorris@martin.biz",
#       "partnerCode": "8ac8f7a6-aefe-407e-85d7-91a4b1ecc002"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2005-07-02T23:01:41.345005",
#     "leaseStartDate": "2026-01-14",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Ariel",
#       "secondName": "Oneal",
#       "email": "ryandodson@example.com",
#       "mobile": "001-253-657-4213x78077"
#     },
#     "address": {
#       "text": "09361 Sylvia Viaduct\nLake Kellyborough, ME 92463",
#       "unit": "24",
#       "streetNumber": "223",
#       "streetName": "Lopez Wall",
#       "locality": "Pamstad",
#       "postCode": 1125,
#       "state": "Tennessee",
#       "city": "New Angelaland",
#       "country": "Saint Kitts and Nevis"
#     },
#     "referringAgent": {
#       "name": "Thomas Stuart",
#       "email": "ojones@example.org",
#       "partnerCode": "034615c1-80dc-4faf-bc8b-6f303e80caac"
#     },
#     "referringAgency": {
#       "name": "Pruitt Ltd",
#       "email": "jameschase@alvarado-ingram.net",
#       "partnerCode": "9f7e6367-1984-4125-8828-78ba1ab8ffcc"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2006-03-24T08:34:59.283817",
#     "leaseStartDate": "2025-09-24",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Chelsea",
#       "secondName": "Sherman",
#       "email": "kelleyjacqueline@example.com",
#       "mobile": "395.225.8879x42890"
#     },
#     "address": {
#       "text": "89111 Rodriguez Ports Suite 856\nAguilarmouth, MT 03513",
#       "unit": "30",
#       "streetNumber": "320",
#       "streetName": "Courtney Way",
#       "locality": "Toddchester",
#       "postCode": 4365,
#       "state": "Indiana",
#       "city": "West Patrickberg",
#       "country": "Peru"
#     },
#     "referringAgent": {
#       "name": "Alan Berry",
#       "email": "atkinsmichelle@example.com",
#       "partnerCode": "8b0dddfb-6aef-4f11-b0a5-7936c98035e3"
#     },
#     "referringAgency": {
#       "name": "Smith Inc",
#       "email": "mckenziejohnson@rodriguez.com",
#       "partnerCode": "231fb67d-ba9b-4655-bad3-2b9b008822e4"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2006-11-19T13:05:24.507604",
#     "leaseStartDate": "2026-01-28",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jason",
#       "secondName": "Kim",
#       "email": "spena@example.net",
#       "mobile": "(784)917-0539x28812"
#     },
#     "address": {
#       "text": "90489 Bryan Gardens\nWashingtonborough, WA 05878",
#       "unit": "38",
#       "streetNumber": "202",
#       "streetName": "Frye Circles",
#       "locality": "West Williammouth",
#       "postCode": 6914,
#       "state": "Colorado",
#       "city": "South Johnhaven",
#       "country": "Yemen"
#     },
#     "referringAgent": {
#       "name": "Anthony Williams",
#       "email": "dmeza@example.org",
#       "partnerCode": "611301b7-3a37-4d05-a17d-48e3b6560228"
#     },
#     "referringAgency": {
#       "name": "Gross, Adkins and Leblanc",
#       "email": "janet98@morrison.com",
#       "partnerCode": "622c8900-5d86-45a8-b5ff-ffcf046bac2f"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1990-01-14T03:58:12.687209",
#     "leaseStartDate": "2025-09-04",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Tracy",
#       "secondName": "Mccarthy",
#       "email": "timothy21@example.org",
#       "mobile": "328.682.8079x78398"
#     },
#     "address": {
#       "text": "912 John Estate\nWest Jeremiah, HI 69170",
#       "unit": "15",
#       "streetNumber": "92",
#       "streetName": "Christina Bridge",
#       "locality": "East Jonathan",
#       "postCode": 4761,
#       "state": "Massachusetts",
#       "city": "Leeburgh",
#       "country": "Israel"
#     },
#     "referringAgent": {
#       "name": "Kevin Curtis",
#       "email": "dwhite@example.org",
#       "partnerCode": "e35e173c-334e-42cf-b506-171bb2bdcdf0"
#     },
#     "referringAgency": {
#       "name": "Oneal Inc",
#       "email": "martinbates@beltran-robinson.com",
#       "partnerCode": "bc6488d5-e82f-48ba-98b0-2b422e92c201"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2009-02-22T09:43:37.216521",
#     "leaseStartDate": "2025-11-29",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Michael",
#       "secondName": "Nielsen",
#       "email": "lee62@example.org",
#       "mobile": "+1-623-541-8566x1253"
#     },
#     "address": {
#       "text": "750 Justin Flats Apt. 645\nEast Bradley, AK 02800",
#       "unit": "23",
#       "streetNumber": "444",
#       "streetName": "Walker Meadow",
#       "locality": "Chanburgh",
#       "postCode": 7924,
#       "state": "North Dakota",
#       "city": "Harrisstad",
#       "country": "United States of America"
#     },
#     "referringAgent": {
#       "name": "Jaime Holden",
#       "email": "kellihall@example.net",
#       "partnerCode": "803cbade-5ad3-4b9f-b674-90fef864de5b"
#     },
#     "referringAgency": {
#       "name": "Allen-Bowers",
#       "email": "qthomas@diaz.org",
#       "partnerCode": "14fd5eff-f2d5-45e7-a662-14a18e5344c8"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2000-03-24T09:02:15.949447",
#     "leaseStartDate": "2025-03-30",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Kelly",
#       "secondName": "Russo",
#       "email": "tammywalters@example.org",
#       "mobile": "5824842963"
#     },
#     "address": {
#       "text": "97722 Mary Ramp Apt. 750\nNew Julieside, MP 30881",
#       "unit": "1",
#       "streetNumber": "33",
#       "streetName": "Cortez Oval",
#       "locality": "Williechester",
#       "postCode": 1744,
#       "state": "Georgia",
#       "city": "North Cynthia",
#       "country": "Comoros"
#     },
#     "referringAgent": {
#       "name": "Victoria Parker",
#       "email": "molinajoshua@example.net",
#       "partnerCode": "b15c7ba7-e640-43bd-b380-751b3508c4c2"
#     },
#     "referringAgency": {
#       "name": "Simpson, Jenkins and Hebert",
#       "email": "jeffery83@brown.com",
#       "partnerCode": "6d3da1cd-b351-4cc5-9dff-a51c600b2d5b"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2021-01-15T18:27:57.334291",
#     "leaseStartDate": "2025-03-19",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Ryan",
#       "secondName": "Tucker",
#       "email": "colemanemily@example.net",
#       "mobile": "+1-308-876-1678x4938"
#     },
#     "address": {
#       "text": "10801 Powell Bridge\nJefferyberg, WY 89609",
#       "unit": "17",
#       "streetNumber": "13",
#       "streetName": "Steven Club",
#       "locality": "South Amybury",
#       "postCode": 8914,
#       "state": "Florida",
#       "city": "Danielsview",
#       "country": "Kenya"
#     },
#     "referringAgent": {
#       "name": "Lauren Rojas",
#       "email": "johnnorman@example.org",
#       "partnerCode": "4115fc0a-b04f-45ee-a727-2cf4941a5c08"
#     },
#     "referringAgency": {
#       "name": "Pratt-Clark",
#       "email": "emorales@brown-johnson.info",
#       "partnerCode": "d76a5346-687a-4b7e-bbdb-2060067254b0"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2008-01-16T17:05:33.518222",
#     "leaseStartDate": "2025-12-30",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Kimberly",
#       "secondName": "Hughes",
#       "email": "devin42@example.com",
#       "mobile": "289.588.1044x538"
#     },
#     "address": {
#       "text": "58715 Edward Cove\nValenciaborough, PA 96856",
#       "unit": "49",
#       "streetNumber": "115",
#       "streetName": "Waters Bypass",
#       "locality": "Port Aaron",
#       "postCode": 2389,
#       "state": "Delaware",
#       "city": "East Sophia",
#       "country": "Ghana"
#     },
#     "referringAgent": {
#       "name": "Michael Jimenez",
#       "email": "yrobinson@example.com",
#       "partnerCode": "5f62fb25-0ec2-40e9-aafd-308b78301366"
#     },
#     "referringAgency": {
#       "name": "Joseph, Romero and Taylor",
#       "email": "michealhooper@hamilton-rodriguez.com",
#       "partnerCode": "8e354a26-f5d2-4c35-9123-67305c92535d"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1972-07-28T10:49:39.971624",
#     "leaseStartDate": "2025-05-28",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Sarah",
#       "secondName": "Reynolds",
#       "email": "ikirby@example.org",
#       "mobile": "+1-355-273-2000x5182"
#     },
#     "address": {
#       "text": "330 Mccullough Lock Suite 462\nOrtegaberg, ME 20135",
#       "unit": "12",
#       "streetNumber": "489",
#       "streetName": "James Pike",
#       "locality": "West Justin",
#       "postCode": 4457,
#       "state": "Tennessee",
#       "city": "Lake Kaylaburgh",
#       "country": "Philippines"
#     },
#     "referringAgent": {
#       "name": "Caleb Thompson",
#       "email": "alejandra47@example.org",
#       "partnerCode": "a9493df6-9ae1-442a-8662-776f25a38041"
#     },
#     "referringAgency": {
#       "name": "Jones PLC",
#       "email": "charlesgarcia@stone.net",
#       "partnerCode": "b09afd70-3067-4cc8-bd98-0405e7809ff4"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1995-06-15T14:18:32.492953",
#     "leaseStartDate": "2026-02-15",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Michael",
#       "secondName": "Warren",
#       "email": "hhawkins@example.org",
#       "mobile": "(800)815-6975x481"
#     },
#     "address": {
#       "text": "9475 David Plains Suite 194\nWilliamsberg, IL 42785",
#       "unit": "35",
#       "streetNumber": "393",
#       "streetName": "James Stravenue",
#       "locality": "Port Danny",
#       "postCode": 4344,
#       "state": "Montana",
#       "city": "Wagnerton",
#       "country": "Trinidad and Tobago"
#     },
#     "referringAgent": {
#       "name": "Jessica Bray",
#       "email": "tarabrandt@example.org",
#       "partnerCode": "4fe7244f-3b3a-4312-9467-0e125e27b41c"
#     },
#     "referringAgency": {
#       "name": "Ross-Mcbride",
#       "email": "parsonskyle@miller.info",
#       "partnerCode": "50b208f3-d134-4111-ab09-909cc46dc0af"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1995-09-25T13:11:23.821893",
#     "leaseStartDate": "2026-02-10",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Vincent",
#       "secondName": "Dennis",
#       "email": "cwang@example.org",
#       "mobile": "001-299-253-4480x288"
#     },
#     "address": {
#       "text": "314 Tristan Mountain Apt. 265\nSmithmouth, IN 35718",
#       "unit": "6",
#       "streetNumber": "268",
#       "streetName": "Marc Courts",
#       "locality": "Nicholasville",
#       "postCode": 5288,
#       "state": "Nevada",
#       "city": "North Mary",
#       "country": "Somalia"
#     },
#     "referringAgent": {
#       "name": "Cheryl Schneider",
#       "email": "charlesmiller@example.org",
#       "partnerCode": "22be41e7-4ff2-4b1f-81da-a9a23855cbca"
#     },
#     "referringAgency": {
#       "name": "Henry-Warren",
#       "email": "brandon50@dawson-kerr.net",
#       "partnerCode": "d859a9a7-160b-4af9-ba5f-acb3c0303d8c"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2001-04-08T22:02:21.193261",
#     "leaseStartDate": "2025-03-21",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Larry",
#       "secondName": "Thompson",
#       "email": "agibbs@example.org",
#       "mobile": "(967)232-4416"
#     },
#     "address": {
#       "text": "317 Dana Bypass\nSmithtown, MH 11624",
#       "unit": "3",
#       "streetNumber": "483",
#       "streetName": "Erica Knoll",
#       "locality": "Wardside",
#       "postCode": 2405,
#       "state": "Michigan",
#       "city": "Nortonport",
#       "country": "British Virgin Islands"
#     },
#     "referringAgent": {
#       "name": "Randy Mora",
#       "email": "changsierra@example.com",
#       "partnerCode": "21b026cd-8bae-4685-b6ae-10511041889b"
#     },
#     "referringAgency": {
#       "name": "Lee, Anderson and Thompson",
#       "email": "qfleming@robinson.net",
#       "partnerCode": "b1841a32-40d1-4457-8ed0-aa44b95bf181"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1986-05-08T17:30:41.652479",
#     "leaseStartDate": "2025-04-05",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "James",
#       "secondName": "Wood",
#       "email": "lorifields@example.org",
#       "mobile": "524.882.8291"
#     },
#     "address": {
#       "text": "6026 Barnes Pines Suite 566\nNorth Antonio, KY 40805",
#       "unit": "16",
#       "streetNumber": "422",
#       "streetName": "Collins Rapid",
#       "locality": "Denisestad",
#       "postCode": 9671,
#       "state": "West Virginia",
#       "city": "Davidton",
#       "country": "Timor-Leste"
#     },
#     "referringAgent": {
#       "name": "Willie Stevenson",
#       "email": "rossmorgan@example.org",
#       "partnerCode": "8b856a8f-f4d4-4032-b703-e29c1958d3d5"
#     },
#     "referringAgency": {
#       "name": "Parks, Roberts and Smith",
#       "email": "williamsmichael@townsend-cook.com",
#       "partnerCode": "ac56f387-53cb-4848-8c1e-aeca0c53a7d7"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1987-05-27T14:50:23.973995",
#     "leaseStartDate": "2025-10-12",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "George",
#       "secondName": "Burke",
#       "email": "robertmoody@example.net",
#       "mobile": "311.914.4537x865"
#     },
#     "address": {
#       "text": "71577 Jessica Villages Apt. 841\nThompsonville, MO 00607",
#       "unit": "33",
#       "streetNumber": "105",
#       "streetName": "Scott Trace",
#       "locality": "Melissafort",
#       "postCode": 2129,
#       "state": "Illinois",
#       "city": "Williamstad",
#       "country": "Libyan Arab Jamahiriya"
#     },
#     "referringAgent": {
#       "name": "Jesus Davidson",
#       "email": "leonard66@example.org",
#       "partnerCode": "ca051542-ebd2-40c2-90a2-2697980bdb0d"
#     },
#     "referringAgency": {
#       "name": "Evans, Avila and Rubio",
#       "email": "brandon86@fuentes-gay.org",
#       "partnerCode": "27b85fed-2c43-4071-93ac-a823202f3d88"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2024-01-02T03:49:17.571957",
#     "leaseStartDate": "2025-07-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Tristan",
#       "secondName": "Small",
#       "email": "judy18@example.com",
#       "mobile": "773.901.6457x9727"
#     },
#     "address": {
#       "text": "8504 Christina Lights\nKatherineville, AK 42243",
#       "unit": "34",
#       "streetNumber": "153",
#       "streetName": "Cole Fall",
#       "locality": "New Mark",
#       "postCode": 3673,
#       "state": "Iowa",
#       "city": "North Daniellemouth",
#       "country": "Bulgaria"
#     },
#     "referringAgent": {
#       "name": "Bryan Ryan",
#       "email": "joyce21@example.org",
#       "partnerCode": "51d3f2e8-f288-4ce5-a18f-fa5d23d8c6a3"
#     },
#     "referringAgency": {
#       "name": "Craig Inc",
#       "email": "john30@ortega-ward.org",
#       "partnerCode": "e2785df1-85ab-40e6-b98a-3d88dddd9334"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1999-04-09T07:42:50.779587",
#     "leaseStartDate": "2025-04-10",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Jonathan",
#       "secondName": "Butler",
#       "email": "wnicholson@example.net",
#       "mobile": "+1-554-292-0129x30677"
#     },
#     "address": {
#       "text": "242 Figueroa Mission\nColeshire, AS 06176",
#       "unit": "38",
#       "streetNumber": "422",
#       "streetName": "Reyes Extension",
#       "locality": "North Todd",
#       "postCode": 1940,
#       "state": "Utah",
#       "city": "North Kristen",
#       "country": "Papua New Guinea"
#     },
#     "referringAgent": {
#       "name": "Jonathan Bailey",
#       "email": "ucooper@example.net",
#       "partnerCode": "3b16e030-8b62-4392-a853-036aceed2d61"
#     },
#     "referringAgency": {
#       "name": "Reynolds, Green and Wolf",
#       "email": "smithzachary@martinez.com",
#       "partnerCode": "ad5dd4ff-8e15-4cc9-98d4-c0828c6749db"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1993-01-11T15:32:34.311747",
#     "leaseStartDate": "2025-05-13",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "James",
#       "secondName": "Kelly",
#       "email": "martinezjoseph@example.net",
#       "mobile": "645.938.6774x6697"
#     },
#     "address": {
#       "text": "5932 Cole Courts Suite 079\nPort Roger, MO 93260",
#       "unit": "16",
#       "streetNumber": "348",
#       "streetName": "Sharon Crossroad",
#       "locality": "Ballardchester",
#       "postCode": 8683,
#       "state": "Georgia",
#       "city": "West Michaelfurt",
#       "country": "Guyana"
#     },
#     "referringAgent": {
#       "name": "Jocelyn Oliver",
#       "email": "courtney93@example.org",
#       "partnerCode": "b6bf12f9-83ac-464d-b823-85df9f5667f9"
#     },
#     "referringAgency": {
#       "name": "Wood Inc",
#       "email": "bennettpatricia@figueroa.net",
#       "partnerCode": "ba9e9d6d-1bb8-4d15-a4cf-c8b07791255c"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2005-11-13T01:47:57.272619",
#     "leaseStartDate": "2026-03-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Brian",
#       "secondName": "Koch",
#       "email": "rick38@example.net",
#       "mobile": "001-567-443-4225"
#     },
#     "address": {
#       "text": "254 Jerome Neck Suite 512\nFieldsview, HI 49951",
#       "unit": "23",
#       "streetNumber": "337",
#       "streetName": "Rocha Drive",
#       "locality": "Lake Joshua",
#       "postCode": 5008,
#       "state": "Idaho",
#       "city": "Perkinsfurt",
#       "country": "Guyana"
#     },
#     "referringAgent": {
#       "name": "Nancy Ford",
#       "email": "nicholas59@example.org",
#       "partnerCode": "48b789dc-1d60-4df0-b944-28159126dc52"
#     },
#     "referringAgency": {
#       "name": "Perez-Reyes",
#       "email": "klowe@wolfe.net",
#       "partnerCode": "29a46b66-863a-49d7-adee-a3ecbb7c3174"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1970-01-13T19:20:56.916182",
#     "leaseStartDate": "2025-05-26",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Kathryn",
#       "secondName": "Boone",
#       "email": "npena@example.org",
#       "mobile": "524.330.1547x677"
#     },
#     "address": {
#       "text": "Unit 4735 Box 0773\nDPO AE 71369",
#       "unit": "21",
#       "streetNumber": "29",
#       "streetName": "Smith Fall",
#       "locality": "Lake Amy",
#       "postCode": 7065,
#       "state": "Oklahoma",
#       "city": "Richardshire",
#       "country": "Canada"
#     },
#     "referringAgent": {
#       "name": "Danielle Sanchez",
#       "email": "rgrant@example.net",
#       "partnerCode": "d07af4cb-c196-4220-8714-a7658b6eeb67"
#     },
#     "referringAgency": {
#       "name": "Baker, Gibson and Banks",
#       "email": "karafreeman@barber.biz",
#       "partnerCode": "5e3fcc5b-90b2-4787-b450-28609227bbdb"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1982-12-10T14:05:36.955054",
#     "leaseStartDate": "2025-04-27",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Tyler",
#       "secondName": "Jones",
#       "email": "justin32@example.com",
#       "mobile": "5213214793"
#     },
#     "address": {
#       "text": "22703 Bender Station\nNorth Amy, RI 09971",
#       "unit": "19",
#       "streetNumber": "354",
#       "streetName": "Sara Turnpike",
#       "locality": "Sarahberg",
#       "postCode": 3234,
#       "state": "Pennsylvania",
#       "city": "Patriciaburgh",
#       "country": "United Arab Emirates"
#     },
#     "referringAgent": {
#       "name": "Patricia Gaines",
#       "email": "bradshawdeborah@example.com",
#       "partnerCode": "c9b6162b-12e3-417d-bd9e-248449b29de9"
#     },
#     "referringAgency": {
#       "name": "Smith, Russo and Ramsey",
#       "email": "brian33@lopez-kline.org",
#       "partnerCode": "0f3871fb-4ef4-4b0a-a94b-67f5d9a38e11"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1983-06-13T07:50:42.083414",
#     "leaseStartDate": "2025-07-07",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jeremy",
#       "secondName": "Houston",
#       "email": "wjackson@example.org",
#       "mobile": "783.809.9594"
#     },
#     "address": {
#       "text": "72688 William Ridge\nPort Jennifer, NE 14465",
#       "unit": "35",
#       "streetNumber": "353",
#       "streetName": "Dennis Glens",
#       "locality": "New Amandastad",
#       "postCode": 4147,
#       "state": "Texas",
#       "city": "Timothymouth",
#       "country": "Cape Verde"
#     },
#     "referringAgent": {
#       "name": "Natalie Peterson",
#       "email": "amberperez@example.net",
#       "partnerCode": "eafe45f6-1368-41e6-a596-b30a7758e8a8"
#     },
#     "referringAgency": {
#       "name": "Smith, Blair and Williams",
#       "email": "markpatrick@peterson-martin.net",
#       "partnerCode": "a8bc3e4e-2180-45c5-a742-00196c846d93"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2003-08-26T11:42:44.557589",
#     "leaseStartDate": "2025-04-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "David",
#       "secondName": "Smith",
#       "email": "karenweber@example.com",
#       "mobile": "(716)830-4283x75004"
#     },
#     "address": {
#       "text": "119 Robertson Mission Apt. 507\nWest Alexis, AZ 57116",
#       "unit": "27",
#       "streetNumber": "164",
#       "streetName": "Campbell Coves",
#       "locality": "Port Jennifer",
#       "postCode": 4219,
#       "state": "North Carolina",
#       "city": "South Jenniferstad",
#       "country": "Aruba"
#     },
#     "referringAgent": {
#       "name": "Diamond Powers",
#       "email": "ldiaz@example.org",
#       "partnerCode": "7f8fde5d-18be-4cb5-9d1b-bd2c4d36bd84"
#     },
#     "referringAgency": {
#       "name": "Flores PLC",
#       "email": "thomascurry@meyers.info",
#       "partnerCode": "460a12e3-f28c-4673-9472-707481dc9e0a"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1983-06-04T18:52:39.098477",
#     "leaseStartDate": "2025-04-01",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Christian",
#       "secondName": "Wilson",
#       "email": "wintersanthony@example.org",
#       "mobile": "+1-335-930-2458x2570"
#     },
#     "address": {
#       "text": "013 Amy Crescent Apt. 007\nWest Curtis, HI 78080",
#       "unit": "19",
#       "streetNumber": "232",
#       "streetName": "Michael Prairie",
#       "locality": "South Samuel",
#       "postCode": 2056,
#       "state": "Washington",
#       "city": "Clarkside",
#       "country": "Turks and Caicos Islands"
#     },
#     "referringAgent": {
#       "name": "Michelle Blair",
#       "email": "christopherhill@example.org",
#       "partnerCode": "b7a24f54-c452-4fc8-8071-a5983bdcc3f5"
#     },
#     "referringAgency": {
#       "name": "Miller, Hernandez and Soto",
#       "email": "ruizbenjamin@smith.com",
#       "partnerCode": "3ca86ea0-eb41-467e-b012-78e376b763bb"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1981-08-11T14:06:36.679170",
#     "leaseStartDate": "2025-08-27",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Joanne",
#       "secondName": "Gutierrez",
#       "email": "mwhite@example.com",
#       "mobile": "6585184380"
#     },
#     "address": {
#       "text": "3113 Richard Rest Apt. 840\nSouth Kelli, ID 60134",
#       "unit": "30",
#       "streetNumber": "428",
#       "streetName": "Patterson Grove",
#       "locality": "Gloriamouth",
#       "postCode": 6674,
#       "state": "Alabama",
#       "city": "North Samuelshire",
#       "country": "British Virgin Islands"
#     },
#     "referringAgent": {
#       "name": "Brian Myers",
#       "email": "jackwallace@example.com",
#       "partnerCode": "18e7808f-9264-430f-a9f6-2282a6655475"
#     },
#     "referringAgency": {
#       "name": "Jackson, Nguyen and Wiggins",
#       "email": "heathergonzalez@christensen-johnson.org",
#       "partnerCode": "9c677a34-b07d-462d-9bcf-c8b91c89c3eb"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1978-07-08T18:28:19.282844",
#     "leaseStartDate": "2025-08-05",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Edward",
#       "secondName": "Chang",
#       "email": "lawsonkristina@example.com",
#       "mobile": "486-459-0039"
#     },
#     "address": {
#       "text": "863 Diaz Gateway Suite 522\nRivasview, FL 47881",
#       "unit": "40",
#       "streetNumber": "479",
#       "streetName": "Nicole Terrace",
#       "locality": "Lake Michael",
#       "postCode": 1749,
#       "state": "Missouri",
#       "city": "Eugenechester",
#       "country": "Wallis and Futuna"
#     },
#     "referringAgent": {
#       "name": "Kenneth Ramos",
#       "email": "jameszachary@example.org",
#       "partnerCode": "bc6659d2-5bdc-4c45-bcac-f84dbab3b3ae"
#     },
#     "referringAgency": {
#       "name": "White and Sons",
#       "email": "chelsea29@morris-smith.com",
#       "partnerCode": "dfa66763-1ade-4464-8eea-2f4ade78b1a8"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2015-11-19T15:32:11.032454",
#     "leaseStartDate": "2025-07-08",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Michael",
#       "secondName": "Medina",
#       "email": "morrisbeth@example.org",
#       "mobile": "001-681-568-8925"
#     },
#     "address": {
#       "text": "67003 Booker Grove\nBrandyshire, NY 74153",
#       "unit": "4",
#       "streetNumber": "277",
#       "streetName": "Tracy Loaf",
#       "locality": "Randystad",
#       "postCode": 4958,
#       "state": "New York",
#       "city": "East Jermaine",
#       "country": "Oman"
#     },
#     "referringAgent": {
#       "name": "Jessica Nichols",
#       "email": "fcohen@example.org",
#       "partnerCode": "ab5c2764-9442-410b-abc7-27e0accac173"
#     },
#     "referringAgency": {
#       "name": "Vasquez Ltd",
#       "email": "rogersteresa@andersen-olson.com",
#       "partnerCode": "ac2b41a9-d2c8-4fab-ac8f-d3f5fa99b8b1"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2001-01-18T01:18:19.647532",
#     "leaseStartDate": "2025-04-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Keith",
#       "secondName": "Taylor",
#       "email": "robertruiz@example.com",
#       "mobile": "640-272-6299"
#     },
#     "address": {
#       "text": "16134 Morrow Extension Apt. 369\nJensenburgh, NV 46535",
#       "unit": "10",
#       "streetNumber": "447",
#       "streetName": "Freeman Rest",
#       "locality": "Lake Kathy",
#       "postCode": 7214,
#       "state": "Maine",
#       "city": "North Hollyville",
#       "country": "Samoa"
#     },
#     "referringAgent": {
#       "name": "Paula Wood",
#       "email": "johnsonantonio@example.org",
#       "partnerCode": "a47652d2-f56d-433b-a3b7-5574ecca22de"
#     },
#     "referringAgency": {
#       "name": "Preston Ltd",
#       "email": "john31@rivas.org",
#       "partnerCode": "4facc3fd-7530-4269-b19d-b412b7b2e270"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1986-06-05T01:00:09.165606",
#     "leaseStartDate": "2026-01-26",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "David",
#       "secondName": "Rivera",
#       "email": "egarrett@example.org",
#       "mobile": "+1-806-922-4334x7904"
#     },
#     "address": {
#       "text": "2022 Smith Squares Apt. 380\nClarkview, AL 83242",
#       "unit": "18",
#       "streetNumber": "63",
#       "streetName": "Marissa Haven",
#       "locality": "North Jamesfort",
#       "postCode": 8294,
#       "state": "South Carolina",
#       "city": "Jamesbury",
#       "country": "Netherlands"
#     },
#     "referringAgent": {
#       "name": "David Martinez MD",
#       "email": "robert25@example.net",
#       "partnerCode": "005c6a86-0b0e-4be7-9b41-da4e020d4690"
#     },
#     "referringAgency": {
#       "name": "Randolph-Garcia",
#       "email": "carrie57@baxter-holmes.com",
#       "partnerCode": "aab92bf0-d1ae-4070-b8c5-33edd481490c"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2002-11-22T02:18:00.785857",
#     "leaseStartDate": "2026-01-18",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Dana",
#       "secondName": "Davis",
#       "email": "amydoyle@example.net",
#       "mobile": "207-546-6240x041"
#     },
#     "address": {
#       "text": "692 Stephanie Field\nCrystalland, OR 12089",
#       "unit": "9",
#       "streetNumber": "77",
#       "streetName": "Cherry Pines",
#       "locality": "South Andrewshire",
#       "postCode": 3660,
#       "state": "Tennessee",
#       "city": "New Stephen",
#       "country": "Senegal"
#     },
#     "referringAgent": {
#       "name": "Lawrence Acevedo",
#       "email": "mallory34@example.com",
#       "partnerCode": "a5509db1-fab9-446a-a607-771c1b8c1d5f"
#     },
#     "referringAgency": {
#       "name": "Flynn, Zhang and Romero",
#       "email": "nelsonmarissa@soto-evans.com",
#       "partnerCode": "8116c833-f2d0-4184-bdc0-ccb40312be1f"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2023-03-31T04:10:35.254756",
#     "leaseStartDate": "2025-11-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Mary",
#       "secondName": "Williams",
#       "email": "cervanteshunter@example.com",
#       "mobile": "634.988.9900"
#     },
#     "address": {
#       "text": "07617 Roberts Walk Suite 451\nWalshhaven, OH 56528",
#       "unit": "49",
#       "streetNumber": "269",
#       "streetName": "Williams Brooks",
#       "locality": "West Ashleyside",
#       "postCode": 2696,
#       "state": "Pennsylvania",
#       "city": "South Andrew",
#       "country": "Mauritius"
#     },
#     "referringAgent": {
#       "name": "Eric Mills",
#       "email": "cgonzalez@example.com",
#       "partnerCode": "5fc0fc77-a4a3-4f71-89e9-2f4527884613"
#     },
#     "referringAgency": {
#       "name": "Ryan, Morales and Pearson",
#       "email": "sanchezjohn@watts.info",
#       "partnerCode": "dd857c54-ca66-4c16-aae7-605d18777028"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1975-02-26T05:40:24.181906",
#     "leaseStartDate": "2025-07-06",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Jeffrey",
#       "secondName": "Jordan",
#       "email": "hlee@example.com",
#       "mobile": "+1-456-400-4116x055"
#     },
#     "address": {
#       "text": "5534 Smith Station\nWest Nathanfort, DE 09483",
#       "unit": "10",
#       "streetNumber": "445",
#       "streetName": "Susan Island",
#       "locality": "Juarezmouth",
#       "postCode": 8795,
#       "state": "Maryland",
#       "city": "West Jasmine",
#       "country": "Bhutan"
#     },
#     "referringAgent": {
#       "name": "Wendy Rodriguez",
#       "email": "vwang@example.org",
#       "partnerCode": "b12f2057-eca1-49ca-aa7a-f00cc0fc37d3"
#     },
#     "referringAgency": {
#       "name": "Rivers-Curry",
#       "email": "othomas@gentry.com",
#       "partnerCode": "81b02cce-66fe-4b81-90bb-c60352ee2d9f"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2006-02-10T09:43:37.998196",
#     "leaseStartDate": "2025-12-17",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Daniel",
#       "secondName": "Joseph",
#       "email": "smcdowell@example.net",
#       "mobile": "6996303601"
#     },
#     "address": {
#       "text": "300 Christina Road Suite 006\nMauriceshire, FL 04028",
#       "unit": "26",
#       "streetNumber": "175",
#       "streetName": "Carla Divide",
#       "locality": "West Justintown",
#       "postCode": 5669,
#       "state": "Missouri",
#       "city": "New Bradley",
#       "country": "United States of America"
#     },
#     "referringAgent": {
#       "name": "Daniel Adams",
#       "email": "charles85@example.org",
#       "partnerCode": "5ae23720-60f7-48e8-b0db-080e90c97988"
#     },
#     "referringAgency": {
#       "name": "Medina, Watkins and Harmon",
#       "email": "williamsadrian@ford-sparks.org",
#       "partnerCode": "c3ee9fc8-7bdd-4c53-a74b-8b4d0cf7c777"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1987-03-06T01:46:09.069169",
#     "leaseStartDate": "2025-11-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Sandra",
#       "secondName": "Sanchez",
#       "email": "uhull@example.net",
#       "mobile": "001-745-638-7119x27558"
#     },
#     "address": {
#       "text": "505 Dorothy Plaza\nThompsonside, NE 92388",
#       "unit": "8",
#       "streetNumber": "457",
#       "streetName": "Holland Cape",
#       "locality": "Port Amy",
#       "postCode": 8057,
#       "state": "Delaware",
#       "city": "Mezastad",
#       "country": "Barbados"
#     },
#     "referringAgent": {
#       "name": "Bryan Harris",
#       "email": "mirandagordon@example.org",
#       "partnerCode": "fe838b70-5b0f-41f6-81be-be7dff3a0667"
#     },
#     "referringAgency": {
#       "name": "Kennedy-Roberts",
#       "email": "karen16@greene.com",
#       "partnerCode": "49a14a37-6d23-4876-98c3-07955926dc5a"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1997-12-17T09:57:15.004000",
#     "leaseStartDate": "2025-06-22",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Eric",
#       "secondName": "Arnold",
#       "email": "jamesjones@example.com",
#       "mobile": "275-636-4657x665"
#     },
#     "address": {
#       "text": "33151 Tyler Avenue Suite 976\nNelsonburgh, WA 94037",
#       "unit": "13",
#       "streetNumber": "61",
#       "streetName": "Hartman Trace",
#       "locality": "Thomashaven",
#       "postCode": 2379,
#       "state": "Delaware",
#       "city": "East Mitchell",
#       "country": "Botswana"
#     },
#     "referringAgent": {
#       "name": "Anthony Garcia",
#       "email": "bbaker@example.net",
#       "partnerCode": "f7d401f0-b888-4596-93f0-8a78e439f6bd"
#     },
#     "referringAgency": {
#       "name": "Gomez, Arias and Cunningham",
#       "email": "rebeccalopez@beard-marks.com",
#       "partnerCode": "42cf889b-006d-4071-8884-bd40b7bf3ce7"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1989-08-19T17:52:03.656547",
#     "leaseStartDate": "2025-10-28",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Robert",
#       "secondName": "Thompson",
#       "email": "rachel97@example.org",
#       "mobile": "265-208-8205x6983"
#     },
#     "address": {
#       "text": "38977 Tamara Crest\nNorth Scott, WV 69931",
#       "unit": "1",
#       "streetNumber": "202",
#       "streetName": "Teresa Drive",
#       "locality": "Port Jefferyton",
#       "postCode": 6315,
#       "state": "Hawaii",
#       "city": "Port Jason",
#       "country": "Tokelau"
#     },
#     "referringAgent": {
#       "name": "David Wells",
#       "email": "ptorres@example.com",
#       "partnerCode": "012965e4-bea8-462c-b72b-7180d7205406"
#     },
#     "referringAgency": {
#       "name": "Black, Foster and Anthony",
#       "email": "duncandeborah@bishop-jones.com",
#       "partnerCode": "551cfa47-d074-494d-9122-db1a1f227964"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1981-09-27T13:43:00.038938",
#     "leaseStartDate": "2025-09-17",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Bruce",
#       "secondName": "Morrison",
#       "email": "kblackwell@example.org",
#       "mobile": "(396)969-3215"
#     },
#     "address": {
#       "text": "7029 Lopez Coves Suite 844\nSnyderchester, KY 39648",
#       "unit": "1",
#       "streetNumber": "408",
#       "streetName": "Richard Hollow",
#       "locality": "East Emily",
#       "postCode": 8581,
#       "state": "New Jersey",
#       "city": "North Jacob",
#       "country": "Saint Helena"
#     },
#     "referringAgent": {
#       "name": "Natalie Brandt",
#       "email": "josephhodges@example.org",
#       "partnerCode": "d0139198-b80e-4a5a-888d-13880a6d76d0"
#     },
#     "referringAgency": {
#       "name": "Ellis-Nguyen",
#       "email": "bhall@ferguson.net",
#       "partnerCode": "b69d18c3-3edd-48bf-a40f-289652ac9cac"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1982-07-09T00:12:04.662047",
#     "leaseStartDate": "2025-10-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Gina",
#       "secondName": "Nicholson",
#       "email": "tony47@example.org",
#       "mobile": "731.984.0416"
#     },
#     "address": {
#       "text": "2580 Alexander Lakes\nReginabury, VI 19364",
#       "unit": "2",
#       "streetNumber": "270",
#       "streetName": "Thornton Fields",
#       "locality": "Andersontown",
#       "postCode": 3592,
#       "state": "Montana",
#       "city": "Lawrencetown",
#       "country": "British Virgin Islands"
#     },
#     "referringAgent": {
#       "name": "Joshua Brown",
#       "email": "brendawhite@example.net",
#       "partnerCode": "8faba4fc-3377-49ef-9d2d-f6f71156e7ec"
#     },
#     "referringAgency": {
#       "name": "Rogers, Owens and Odonnell",
#       "email": "ashleygray@aguilar-young.net",
#       "partnerCode": "0824052a-fdce-4f70-b74b-2e7c371c56e9"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2003-05-04T21:10:49.788715",
#     "leaseStartDate": "2025-12-16",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Heather",
#       "secondName": "Mathis",
#       "email": "ylong@example.org",
#       "mobile": "277.921.9137"
#     },
#     "address": {
#       "text": "USNV Steele\nFPO AP 70069",
#       "unit": "39",
#       "streetNumber": "68",
#       "streetName": "Gregory Park",
#       "locality": "Garciafort",
#       "postCode": 6199,
#       "state": "Louisiana",
#       "city": "South Anthonyfurt",
#       "country": "Timor-Leste"
#     },
#     "referringAgent": {
#       "name": "Colton Moore",
#       "email": "michael99@example.org",
#       "partnerCode": "1506beae-12f5-4071-b92d-95903db0da44"
#     },
#     "referringAgency": {
#       "name": "Hart-White",
#       "email": "douglas58@mendoza.com",
#       "partnerCode": "2693ad41-c0f5-4eea-aa66-ffdc04f0726b"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2022-10-31T03:04:51.927502",
#     "leaseStartDate": "2026-01-28",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Kevin",
#       "secondName": "Cuevas",
#       "email": "anthonysmith@example.com",
#       "mobile": "(824)738-5407"
#     },
#     "address": {
#       "text": "1768 David Junction\nSouth Candicetown, PW 94453",
#       "unit": "17",
#       "streetNumber": "469",
#       "streetName": "Ryan Pass",
#       "locality": "Millerberg",
#       "postCode": 5110,
#       "state": "Nebraska",
#       "city": "Lake Nicholasborough",
#       "country": "Marshall Islands"
#     },
#     "referringAgent": {
#       "name": "Elizabeth Brown",
#       "email": "hannah77@example.org",
#       "partnerCode": "b6753803-c1af-45ac-aee6-1e3eda849e08"
#     },
#     "referringAgency": {
#       "name": "Thomas Inc",
#       "email": "mackstephen@saunders.com",
#       "partnerCode": "9451303a-f324-4937-b07e-9804b67e83df"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1983-09-13T15:54:50.813560",
#     "leaseStartDate": "2026-02-23",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Sarah",
#       "secondName": "Mendoza",
#       "email": "mferguson@example.com",
#       "mobile": "7519701962"
#     },
#     "address": {
#       "text": "69679 Michael Camp\nMichaelburgh, MP 31738",
#       "unit": "30",
#       "streetNumber": "298",
#       "streetName": "Jackie Way",
#       "locality": "South Gloriahaven",
#       "postCode": 7178,
#       "state": "Louisiana",
#       "city": "Wilsonside",
#       "country": "Mauritius"
#     },
#     "referringAgent": {
#       "name": "Jeremy Brown",
#       "email": "tracey42@example.net",
#       "partnerCode": "547e8e36-e8b1-4980-b9f1-b7b19a421795"
#     },
#     "referringAgency": {
#       "name": "Wilcox, Hernandez and Kaiser",
#       "email": "wilsonfrancisco@reyes.net",
#       "partnerCode": "aca021f4-2844-4dbf-be04-e14c4de7291a"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2023-12-10T16:43:14.713505",
#     "leaseStartDate": "2025-11-04",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Brenda",
#       "secondName": "Jennings",
#       "email": "amy69@example.org",
#       "mobile": "001-813-841-9549x7120"
#     },
#     "address": {
#       "text": "USNS Reynolds\nFPO AA 04356",
#       "unit": "38",
#       "streetNumber": "73",
#       "streetName": "Sims Trafficway",
#       "locality": "New Patricia",
#       "postCode": 5039,
#       "state": "Hawaii",
#       "city": "South Angelastad",
#       "country": "Bahamas"
#     },
#     "referringAgent": {
#       "name": "Angela Crawford",
#       "email": "coltonfrey@example.com",
#       "partnerCode": "2616b216-54bb-4bdc-9191-46651be4cf47"
#     },
#     "referringAgency": {
#       "name": "Wilson, Wells and Henson",
#       "email": "chad88@acevedo-wheeler.org",
#       "partnerCode": "5c376167-fec5-4f5e-8400-b3a3f35649a4"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1989-12-03T13:48:00.834165",
#     "leaseStartDate": "2025-06-01",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jennifer",
#       "secondName": "Pennington",
#       "email": "natalie85@example.com",
#       "mobile": "247.345.2278x200"
#     },
#     "address": {
#       "text": "416 Dillon Path Suite 259\nEvansberg, OR 05553",
#       "unit": "26",
#       "streetNumber": "348",
#       "streetName": "Rachel Plaza",
#       "locality": "South Darrellhaven",
#       "postCode": 1476,
#       "state": "Washington",
#       "city": "North Elizabeth",
#       "country": "Anguilla"
#     },
#     "referringAgent": {
#       "name": "Rebecca Taylor",
#       "email": "poconnor@example.org",
#       "partnerCode": "4a98d106-31e0-4b98-bbec-cdd0b0441911"
#     },
#     "referringAgency": {
#       "name": "James Inc",
#       "email": "mariavalencia@jones-brock.com",
#       "partnerCode": "ec000964-238b-436a-9e4e-515b574b19fc"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2001-03-31T22:27:13.414262",
#     "leaseStartDate": "2025-10-16",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Amanda",
#       "secondName": "Griffin",
#       "email": "tammy40@example.net",
#       "mobile": "640.846.0200x892"
#     },
#     "address": {
#       "text": "626 Thompson Turnpike Suite 202\nMoralestown, WA 28917",
#       "unit": "27",
#       "streetNumber": "243",
#       "streetName": "Johnson Crossing",
#       "locality": "East Brittanyberg",
#       "postCode": 5835,
#       "state": "Oregon",
#       "city": "New David",
#       "country": "Maldives"
#     },
#     "referringAgent": {
#       "name": "Richard Brooks",
#       "email": "turnersara@example.com",
#       "partnerCode": "e98bc874-20d1-4a0d-9070-38d5569cac4a"
#     },
#     "referringAgency": {
#       "name": "Baker Inc",
#       "email": "parsonsmichael@williams-perry.biz",
#       "partnerCode": "8965f713-eb49-4d1f-8203-fa8dde5a5b98"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2004-11-02T10:03:34.917597",
#     "leaseStartDate": "2025-10-11",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jeanette",
#       "secondName": "Kline",
#       "email": "walkerwhitney@example.com",
#       "mobile": "599-361-0875x37543"
#     },
#     "address": {
#       "text": "206 Kimberly Hill\nDeborahton, MP 36156",
#       "unit": "42",
#       "streetNumber": "477",
#       "streetName": "Romero Forks",
#       "locality": "North Caleb",
#       "postCode": 9308,
#       "state": "Iowa",
#       "city": "East Melanie",
#       "country": "Sri Lanka"
#     },
#     "referringAgent": {
#       "name": "Robert Thornton",
#       "email": "brooksbrittany@example.org",
#       "partnerCode": "9fd857fd-3faa-41ba-a73d-01edde36ab2b"
#     },
#     "referringAgency": {
#       "name": "Liu LLC",
#       "email": "nrandolph@macdonald-navarro.net",
#       "partnerCode": "947f60eb-d85a-48a8-b340-69ac49afc823"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1977-07-14T06:35:53.478354",
#     "leaseStartDate": "2025-11-11",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Sara",
#       "secondName": "Guzman",
#       "email": "james68@example.org",
#       "mobile": "001-995-911-3819x52691"
#     },
#     "address": {
#       "text": "Unit 8128 Box 3943\nDPO AP 61636",
#       "unit": "9",
#       "streetNumber": "179",
#       "streetName": "Erik Trace",
#       "locality": "Kathrynhaven",
#       "postCode": 2111,
#       "state": "Kentucky",
#       "city": "West Anthonystad",
#       "country": "Montserrat"
#     },
#     "referringAgent": {
#       "name": "Megan Brown",
#       "email": "nicholasbrown@example.net",
#       "partnerCode": "22ac0f03-fe94-431b-b1fe-ffc219fc9e3c"
#     },
#     "referringAgency": {
#       "name": "Herrera Group",
#       "email": "gloria35@ortiz-brown.com",
#       "partnerCode": "b7ff89fa-2a93-4da1-a654-e53c82d6b020"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2018-02-09T20:36:50.582904",
#     "leaseStartDate": "2026-02-12",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jason",
#       "secondName": "Lewis",
#       "email": "higginsrussell@example.com",
#       "mobile": "+1-554-642-3087"
#     },
#     "address": {
#       "text": "Unit 1832 Box 5544\nDPO AE 07335",
#       "unit": "45",
#       "streetNumber": "279",
#       "streetName": "Velazquez Greens",
#       "locality": "South Denise",
#       "postCode": 6291,
#       "state": "Virginia",
#       "city": "New Jared",
#       "country": "Namibia"
#     },
#     "referringAgent": {
#       "name": "Michael Robinson",
#       "email": "sheltonkyle@example.com",
#       "partnerCode": "ae921f3c-50ef-48e7-bdab-4434649b7f2f"
#     },
#     "referringAgency": {
#       "name": "Medina Inc",
#       "email": "zjackson@henry-shepard.org",
#       "partnerCode": "34d544d3-fb9d-431a-a6c2-57aa70769382"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1989-04-26T02:36:19.640385",
#     "leaseStartDate": "2025-05-01",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Robert",
#       "secondName": "White",
#       "email": "brookscynthia@example.net",
#       "mobile": "3613569341"
#     },
#     "address": {
#       "text": "9513 Chelsea Court Suite 796\nMatthewside, ID 91799",
#       "unit": "12",
#       "streetNumber": "43",
#       "streetName": "Atkins Court",
#       "locality": "North Valeriefurt",
#       "postCode": 8639,
#       "state": "Iowa",
#       "city": "Heatherberg",
#       "country": "Aruba"
#     },
#     "referringAgent": {
#       "name": "Hunter Allen",
#       "email": "adrianluna@example.com",
#       "partnerCode": "6acec0cd-2e3f-46ad-9e7d-050b36459bce"
#     },
#     "referringAgency": {
#       "name": "Armstrong Ltd",
#       "email": "kelleyrenee@khan.biz",
#       "partnerCode": "21fcc51c-8327-4368-812a-67c92eef5334"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2013-07-19T18:54:06.648380",
#     "leaseStartDate": "2025-10-12",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Karen",
#       "secondName": "Mcmahon",
#       "email": "joshua32@example.net",
#       "mobile": "7086455797"
#     },
#     "address": {
#       "text": "41640 Anderson Avenue Apt. 271\nVictorchester, FL 56799",
#       "unit": "7",
#       "streetNumber": "231",
#       "streetName": "Phyllis Knoll",
#       "locality": "Richardborough",
#       "postCode": 9706,
#       "state": "Nevada",
#       "city": "Lake Tracy",
#       "country": "Kyrgyz Republic"
#     },
#     "referringAgent": {
#       "name": "Mrs. Amanda Fisher",
#       "email": "santiagoeric@example.com",
#       "partnerCode": "49eb5bc9-2045-4ad0-83f4-a5cb3a85cc70"
#     },
#     "referringAgency": {
#       "name": "Obrien, Kelly and Brown",
#       "email": "mariafuentes@rogers.com",
#       "partnerCode": "26c5e497-6a1d-4379-930a-8eb871c213d8"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1995-12-06T04:53:57.612651",
#     "leaseStartDate": "2025-05-17",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Stephen",
#       "secondName": "Johnston",
#       "email": "olivia94@example.org",
#       "mobile": "(599)778-3409x87820"
#     },
#     "address": {
#       "text": "8446 Heidi Path\nNorth Veronica, CA 40258",
#       "unit": "12",
#       "streetNumber": "334",
#       "streetName": "Danielle Rue",
#       "locality": "Samuelburgh",
#       "postCode": 9842,
#       "state": "North Carolina",
#       "city": "Isabellaton",
#       "country": "South Georgia and the South Sandwich Islands"
#     },
#     "referringAgent": {
#       "name": "Justin Terry",
#       "email": "xgarcia@example.com",
#       "partnerCode": "23baf341-68a5-42e3-9002-6e951b72f745"
#     },
#     "referringAgency": {
#       "name": "Huff-Phillips",
#       "email": "riveraanthony@gibbs.com",
#       "partnerCode": "422e5248-1309-4316-a13f-bca4196a99f4"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1982-09-19T21:50:06.145623",
#     "leaseStartDate": "2025-11-15",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Matthew",
#       "secondName": "Charles",
#       "email": "onealronnie@example.org",
#       "mobile": "(731)225-9340x40383"
#     },
#     "address": {
#       "text": "890 Kristine Road Apt. 065\nMichaelmouth, MH 12068",
#       "unit": "4",
#       "streetNumber": "332",
#       "streetName": "Collins View",
#       "locality": "New Kristina",
#       "postCode": 9988,
#       "state": "New Jersey",
#       "city": "Shelbymouth",
#       "country": "Dominican Republic"
#     },
#     "referringAgent": {
#       "name": "Rickey Martinez",
#       "email": "fjackson@example.net",
#       "partnerCode": "c3ed269a-9088-49fd-bb4f-62e5cfe014c1"
#     },
#     "referringAgency": {
#       "name": "Foster, Hernandez and Woods",
#       "email": "markcarey@johnson-hess.com",
#       "partnerCode": "c85ae5f0-7f2f-4b24-a82b-d7636ebe08cf"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2006-02-20T07:54:58.622760",
#     "leaseStartDate": "2025-06-04",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Rebecca",
#       "secondName": "Brown",
#       "email": "schwartzandrew@example.org",
#       "mobile": "388-532-0009"
#     },
#     "address": {
#       "text": "749 Long Lodge Suite 530\nEast Alexaport, NJ 19444",
#       "unit": "31",
#       "streetNumber": "206",
#       "streetName": "Christopher Mills",
#       "locality": "New Danielleborough",
#       "postCode": 1250,
#       "state": "South Carolina",
#       "city": "East James",
#       "country": "Luxembourg"
#     },
#     "referringAgent": {
#       "name": "Eric Sanders",
#       "email": "anthonysmall@example.net",
#       "partnerCode": "232c47ab-52b4-494e-8c10-bb3b918603ee"
#     },
#     "referringAgency": {
#       "name": "Baker, Taylor and Curry",
#       "email": "stacey17@hoffman-poole.info",
#       "partnerCode": "b2728f04-e379-40b8-979a-49d75caa821c"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2007-03-11T06:49:13.037657",
#     "leaseStartDate": "2026-01-08",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Debra",
#       "secondName": "Campbell",
#       "email": "pjackson@example.net",
#       "mobile": "+1-264-884-0690x31255"
#     },
#     "address": {
#       "text": "404 Winters Shores\nAndrewborough, PW 92274",
#       "unit": "50",
#       "streetNumber": "474",
#       "streetName": "Romero Manor",
#       "locality": "Kellymouth",
#       "postCode": 4755,
#       "state": "Wisconsin",
#       "city": "Bensontown",
#       "country": "Korea"
#     },
#     "referringAgent": {
#       "name": "Renee Brennan",
#       "email": "xgraham@example.com",
#       "partnerCode": "7965a2c1-60b9-4af5-975a-7721e202660c"
#     },
#     "referringAgency": {
#       "name": "Bell, Mendoza and Wilson",
#       "email": "nicholsonalison@berry.com",
#       "partnerCode": "63c28adc-1c72-410f-96bf-5a57b331bfe9"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2022-09-09T04:07:26.533618",
#     "leaseStartDate": "2026-02-26",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Darren",
#       "secondName": "Lyons",
#       "email": "smithpaul@example.com",
#       "mobile": "518.346.9345x028"
#     },
#     "address": {
#       "text": "0868 Espinoza Forest\nShannonburgh, GU 69472",
#       "unit": "12",
#       "streetNumber": "315",
#       "streetName": "Lopez Courts",
#       "locality": "Port Eric",
#       "postCode": 9633,
#       "state": "Texas",
#       "city": "New Johnport",
#       "country": "French Polynesia"
#     },
#     "referringAgent": {
#       "name": "Brandon Martin",
#       "email": "patriciajones@example.net",
#       "partnerCode": "f7b6db9e-1876-4a51-8c7c-415cec6cab0d"
#     },
#     "referringAgency": {
#       "name": "Kim, Dodson and Johnson",
#       "email": "fordelizabeth@allen.com",
#       "partnerCode": "2a396c83-10d1-4b56-adc1-977f62029295"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1973-11-10T12:11:43.745441",
#     "leaseStartDate": "2025-12-21",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Michael",
#       "secondName": "Villarreal",
#       "email": "anthony97@example.org",
#       "mobile": "+1-308-594-3730x6879"
#     },
#     "address": {
#       "text": "USS Coleman\nFPO AA 31291",
#       "unit": "12",
#       "streetNumber": "72",
#       "streetName": "Wright Square",
#       "locality": "Jacksonville",
#       "postCode": 9384,
#       "state": "Minnesota",
#       "city": "Lake Michael",
#       "country": "Greenland"
#     },
#     "referringAgent": {
#       "name": "Bobby Stark",
#       "email": "ericwhite@example.net",
#       "partnerCode": "29af08b8-a3f0-451b-a0e5-32c1f227a72a"
#     },
#     "referringAgency": {
#       "name": "Duran-Perez",
#       "email": "martinzachary@sanders.biz",
#       "partnerCode": "8c3b7893-7e29-4715-9a90-9c36a9876163"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1988-02-29T14:30:37.741019",
#     "leaseStartDate": "2025-12-27",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Aaron",
#       "secondName": "Salazar",
#       "email": "upierce@example.org",
#       "mobile": "216.357.0017x529"
#     },
#     "address": {
#       "text": "457 Underwood Manor Suite 554\nTaylortown, GA 42280",
#       "unit": "33",
#       "streetNumber": "309",
#       "streetName": "Nelson Lane",
#       "locality": "North Brandy",
#       "postCode": 9191,
#       "state": "Wyoming",
#       "city": "Myersfort",
#       "country": "Suriname"
#     },
#     "referringAgent": {
#       "name": "Lucas Rodriguez",
#       "email": "mark36@example.net",
#       "partnerCode": "28f9b175-be95-415e-9e57-61dbe9a32d88"
#     },
#     "referringAgency": {
#       "name": "Ali, Johnson and Moreno",
#       "email": "kerrygross@brown.info",
#       "partnerCode": "b0cbb7ef-5c5f-4c93-9f3d-a064cfbc94d9"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1972-05-06T10:04:21.974001",
#     "leaseStartDate": "2025-06-27",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Wayne",
#       "secondName": "Wilson",
#       "email": "vjordan@example.com",
#       "mobile": "551-752-8629"
#     },
#     "address": {
#       "text": "463 Mitchell Burgs\nSouth John, FL 80553",
#       "unit": "41",
#       "streetNumber": "321",
#       "streetName": "Jason Knoll",
#       "locality": "East Danielbury",
#       "postCode": 5254,
#       "state": "Arkansas",
#       "city": "West Jessica",
#       "country": "Cote d'Ivoire"
#     },
#     "referringAgent": {
#       "name": "Kristin Clements",
#       "email": "weisskimberly@example.com",
#       "partnerCode": "6f96d3e5-e762-4ca9-bf76-73b194fefbdd"
#     },
#     "referringAgency": {
#       "name": "Davis, Pratt and Jackson",
#       "email": "vreyes@olson-duran.com",
#       "partnerCode": "9a8397b2-eedd-495d-ada6-f50e4e74c1b5"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1985-02-21T05:21:30.170338",
#     "leaseStartDate": "2026-02-17",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Dustin",
#       "secondName": "Moss",
#       "email": "andrew26@example.com",
#       "mobile": "719.517.3396x95738"
#     },
#     "address": {
#       "text": "567 Huffman Well\nMillsstad, ME 52037",
#       "unit": "39",
#       "streetNumber": "229",
#       "streetName": "Watkins Mountain",
#       "locality": "Thomaston",
#       "postCode": 9774,
#       "state": "Kentucky",
#       "city": "Greenland",
#       "country": "Yemen"
#     },
#     "referringAgent": {
#       "name": "Robin Lamb",
#       "email": "kent14@example.com",
#       "partnerCode": "dbacefc7-bf1e-48c8-a925-2056c2aa19c8"
#     },
#     "referringAgency": {
#       "name": "Walker PLC",
#       "email": "heatherfry@burke-griffith.com",
#       "partnerCode": "d9e7d28b-9a26-4d46-9eb8-55497e9ae5ba"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2007-01-08T02:28:18.254276",
#     "leaseStartDate": "2025-11-19",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Deborah",
#       "secondName": "Smith",
#       "email": "kmarshall@example.org",
#       "mobile": "729.700.4823x737"
#     },
#     "address": {
#       "text": "Unit 5901 Box 0499\nDPO AE 28384",
#       "unit": "41",
#       "streetNumber": "216",
#       "streetName": "Jensen Point",
#       "locality": "Farrellburgh",
#       "postCode": 2977,
#       "state": "Idaho",
#       "city": "Goodmanview",
#       "country": "Zimbabwe"
#     },
#     "referringAgent": {
#       "name": "Robert Mcdaniel",
#       "email": "annette84@example.org",
#       "partnerCode": "9498a700-a539-44a7-9595-bcc0164652aa"
#     },
#     "referringAgency": {
#       "name": "Barajas PLC",
#       "email": "amanda35@gomez-adams.com",
#       "partnerCode": "bdfe952f-7e95-41b0-8bfd-549b1dd9f070"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1993-06-30T18:22:53.886924",
#     "leaseStartDate": "2025-11-23",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Matthew",
#       "secondName": "Perkins",
#       "email": "hardylori@example.org",
#       "mobile": "(531)839-0808x4250"
#     },
#     "address": {
#       "text": "PSC 1663, Box 5908\nAPO AA 30584",
#       "unit": "30",
#       "streetNumber": "324",
#       "streetName": "Warren Road",
#       "locality": "Bradfordland",
#       "postCode": 8769,
#       "state": "Mississippi",
#       "city": "Davidview",
#       "country": "Saint Lucia"
#     },
#     "referringAgent": {
#       "name": "Anthony Anderson",
#       "email": "ndavis@example.net",
#       "partnerCode": "4510e2c0-8f0a-471a-97ff-0c18393b62f8"
#     },
#     "referringAgency": {
#       "name": "Garza-Freeman",
#       "email": "lauren13@patterson.org",
#       "partnerCode": "2c7bf2c8-8053-4294-b123-3b362fa5480f"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1996-08-15T08:51:34.288292",
#     "leaseStartDate": "2025-11-13",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Christina",
#       "secondName": "Werner",
#       "email": "bryanjones@example.net",
#       "mobile": "(856)774-4062x803"
#     },
#     "address": {
#       "text": "790 Vargas Drives\nClarkchester, FM 56293",
#       "unit": "13",
#       "streetNumber": "250",
#       "streetName": "Angela Terrace",
#       "locality": "Vickiemouth",
#       "postCode": 2211,
#       "state": "Alabama",
#       "city": "West John",
#       "country": "Kenya"
#     },
#     "referringAgent": {
#       "name": "Brooke Jones",
#       "email": "kevin64@example.net",
#       "partnerCode": "5b4a4a89-9ae3-4819-8250-4de13eb59c33"
#     },
#     "referringAgency": {
#       "name": "Harper and Sons",
#       "email": "thomaspeter@brown.org",
#       "partnerCode": "08cd6053-ed26-46a7-a61b-d35b81d94af2"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1975-10-04T15:30:29.695370",
#     "leaseStartDate": "2026-01-14",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Matthew",
#       "secondName": "Gould",
#       "email": "erinhayes@example.net",
#       "mobile": "(697)733-1843"
#     },
#     "address": {
#       "text": "17959 Cervantes Isle\nNorth Janiceport, SC 03417",
#       "unit": "29",
#       "streetNumber": "452",
#       "streetName": "Garcia Tunnel",
#       "locality": "West Jonathanfurt",
#       "postCode": 8709,
#       "state": "Missouri",
#       "city": "Alexanderside",
#       "country": "Israel"
#     },
#     "referringAgent": {
#       "name": "Melissa Wise DVM",
#       "email": "tcampbell@example.net",
#       "partnerCode": "edcc56fb-27b4-4625-9be0-e5ee1cd2d652"
#     },
#     "referringAgency": {
#       "name": "Bailey Inc",
#       "email": "bgardner@james.com",
#       "partnerCode": "83989f42-e1cb-4616-814b-2807e2b455af"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1998-03-11T06:57:13.485604",
#     "leaseStartDate": "2025-06-27",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Dana",
#       "secondName": "Morrow",
#       "email": "mikecain@example.org",
#       "mobile": "812.759.4235"
#     },
#     "address": {
#       "text": "8956 Taylor Stravenue Suite 367\nEast Thomas, IL 37791",
#       "unit": "8",
#       "streetNumber": "337",
#       "streetName": "Willis Bridge",
#       "locality": "Port Jason",
#       "postCode": 4987,
#       "state": "South Carolina",
#       "city": "Bakerbury",
#       "country": "Serbia"
#     },
#     "referringAgent": {
#       "name": "Steven Franklin MD",
#       "email": "snyderhelen@example.org",
#       "partnerCode": "a81b6925-1ae9-424d-b1d6-8892234d2f66"
#     },
#     "referringAgency": {
#       "name": "Owens, Olson and Marsh",
#       "email": "jonathonbowers@myers-meadows.org",
#       "partnerCode": "6beabade-401f-487b-8a6e-f59c906f0e77"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1977-04-29T11:37:50.905288",
#     "leaseStartDate": "2026-03-04",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Lorraine",
#       "secondName": "Decker",
#       "email": "wheelersandra@example.net",
#       "mobile": "7417720855"
#     },
#     "address": {
#       "text": "076 Jody Circle Apt. 161\nNorth Melanie, CT 40023",
#       "unit": "35",
#       "streetNumber": "426",
#       "streetName": "Lambert Forges",
#       "locality": "Austinton",
#       "postCode": 8859,
#       "state": "Montana",
#       "city": "East Jillborough",
#       "country": "South Georgia and the South Sandwich Islands"
#     },
#     "referringAgent": {
#       "name": "Victoria Watson",
#       "email": "joseph42@example.net",
#       "partnerCode": "6e37186c-5830-4ab8-ba9d-0c9b4132c301"
#     },
#     "referringAgency": {
#       "name": "Guerrero and Sons",
#       "email": "hmorris@medina-neal.com",
#       "partnerCode": "c5d0cdca-af6c-48c8-8f68-d3c28d0eba4f"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1999-02-12T19:11:35.917940",
#     "leaseStartDate": "2025-12-18",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Maria",
#       "secondName": "Harvey",
#       "email": "philipjohnson@example.net",
#       "mobile": "(613)529-6693"
#     },
#     "address": {
#       "text": "1765 Calvin Plaza Suite 414\nFarleyview, DC 58239",
#       "unit": "31",
#       "streetNumber": "85",
#       "streetName": "Reyes Pass",
#       "locality": "South Craig",
#       "postCode": 2685,
#       "state": "Kentucky",
#       "city": "Barbaraton",
#       "country": "Bulgaria"
#     },
#     "referringAgent": {
#       "name": "Rhonda Crawford",
#       "email": "cedwards@example.com",
#       "partnerCode": "b24dda94-7f2a-45c1-8cee-95d9804b2700"
#     },
#     "referringAgency": {
#       "name": "Jackson Inc",
#       "email": "kristen76@morrow.com",
#       "partnerCode": "32b1d24b-dd8c-4c5e-b172-c9ae729828a6"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2012-01-11T16:27:21.562890",
#     "leaseStartDate": "2025-12-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Joyce",
#       "secondName": "Guzman",
#       "email": "ustone@example.net",
#       "mobile": "(615)617-1258x568"
#     },
#     "address": {
#       "text": "14156 Flores Neck\nTroyfurt, MD 21123",
#       "unit": "29",
#       "streetNumber": "459",
#       "streetName": "Amy Estate",
#       "locality": "Port Carrie",
#       "postCode": 1176,
#       "state": "South Dakota",
#       "city": "East Lisa",
#       "country": "Venezuela"
#     },
#     "referringAgent": {
#       "name": "Gabrielle Woods",
#       "email": "lynn66@example.org",
#       "partnerCode": "21a4c16e-1228-469a-9b4e-ebb9fe8f2c0d"
#     },
#     "referringAgency": {
#       "name": "Howell, Powell and Salazar",
#       "email": "morganjohnson@chavez.com",
#       "partnerCode": "ead28a1f-4afd-4061-9fda-48e63498621c"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1999-01-11T09:32:33.829752",
#     "leaseStartDate": "2025-04-25",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Lindsay",
#       "secondName": "Walker",
#       "email": "nmeyer@example.org",
#       "mobile": "+1-854-468-6964x60164"
#     },
#     "address": {
#       "text": "72292 James Bypass\nLake Rebecca, RI 86040",
#       "unit": "16",
#       "streetNumber": "71",
#       "streetName": "Sarah Way",
#       "locality": "East Josemouth",
#       "postCode": 4931,
#       "state": "Wisconsin",
#       "city": "Martinchester",
#       "country": "Norway"
#     },
#     "referringAgent": {
#       "name": "Carrie Skinner",
#       "email": "cindydorsey@example.com",
#       "partnerCode": "b9d28e77-1849-40ba-b7d6-ee3b4c4a3f39"
#     },
#     "referringAgency": {
#       "name": "Thomas-Whitehead",
#       "email": "jenniferrogers@lowe-ramirez.com",
#       "partnerCode": "4d0a30df-d38a-4b60-9a9a-2bccadf5dca4"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1985-09-15T21:38:28.724851",
#     "leaseStartDate": "2025-07-03",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Elizabeth",
#       "secondName": "Roy",
#       "email": "imullins@example.com",
#       "mobile": "(300)716-6937x0951"
#     },
#     "address": {
#       "text": "732 Debra Squares Apt. 065\nElizabethhaven, VA 75091",
#       "unit": "25",
#       "streetNumber": "48",
#       "streetName": "Jill Ports",
#       "locality": "New Kaitlynhaven",
#       "postCode": 4738,
#       "state": "South Carolina",
#       "city": "Lake Joshuashire",
#       "country": "French Guiana"
#     },
#     "referringAgent": {
#       "name": "Amanda Ryan",
#       "email": "kimberly38@example.net",
#       "partnerCode": "06008267-4ccf-4213-bbb0-c796c29eb9cf"
#     },
#     "referringAgency": {
#       "name": "Ward Inc",
#       "email": "alicerivas@stewart.com",
#       "partnerCode": "35acc296-602a-4a9e-8134-db7b928cc1e1"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1996-09-17T10:57:08.993909",
#     "leaseStartDate": "2025-05-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Thomas",
#       "secondName": "Taylor",
#       "email": "watsonlaura@example.net",
#       "mobile": "(401)484-2331"
#     },
#     "address": {
#       "text": "3950 Rose Radial\nPort Tracyfort, ND 65818",
#       "unit": "30",
#       "streetNumber": "119",
#       "streetName": "Tim Valleys",
#       "locality": "Lake Madison",
#       "postCode": 2307,
#       "state": "Illinois",
#       "city": "West Nathanborough",
#       "country": "Portugal"
#     },
#     "referringAgent": {
#       "name": "Lisa Wright",
#       "email": "rlee@example.org",
#       "partnerCode": "8c5f1e39-00cf-4115-a4cf-bf3cd3d2da42"
#     },
#     "referringAgency": {
#       "name": "Williams, Butler and Miller",
#       "email": "gpierce@anthony.org",
#       "partnerCode": "ec1d2354-1e25-41fa-80f1-8c25a710b7d3"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2019-09-19T05:24:27.697565",
#     "leaseStartDate": "2025-03-31",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Brenda",
#       "secondName": "Estes",
#       "email": "ccline@example.net",
#       "mobile": "001-286-389-4304"
#     },
#     "address": {
#       "text": "2671 Charles Ferry Apt. 357\nEast Thomas, PR 19954",
#       "unit": "41",
#       "streetNumber": "19",
#       "streetName": "Austin Islands",
#       "locality": "New Robertchester",
#       "postCode": 2123,
#       "state": "Michigan",
#       "city": "North Charlestown",
#       "country": "Antarctica (the territory South of 60 deg S)"
#     },
#     "referringAgent": {
#       "name": "Katherine Baker",
#       "email": "kwilkins@example.net",
#       "partnerCode": "23c7c1f0-46be-4c10-ac8d-c213f5b108c0"
#     },
#     "referringAgency": {
#       "name": "Holmes-Brown",
#       "email": "matthewsjessica@gonzalez-hopkins.info",
#       "partnerCode": "53e39abe-9b0c-4c03-9c89-c8c3a3fec5cd"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1981-05-19T08:25:49.004527",
#     "leaseStartDate": "2025-10-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Jared",
#       "secondName": "Hess",
#       "email": "eric22@example.net",
#       "mobile": "001-509-899-3333x8706"
#     },
#     "address": {
#       "text": "00394 Stone Stream Apt. 652\nGarciaside, LA 81947",
#       "unit": "22",
#       "streetNumber": "52",
#       "streetName": "Lowe Rapid",
#       "locality": "Lake Hollyville",
#       "postCode": 6492,
#       "state": "Connecticut",
#       "city": "Thomasland",
#       "country": "Guam"
#     },
#     "referringAgent": {
#       "name": "Juan Smith",
#       "email": "amberlee@example.org",
#       "partnerCode": "9f75ce41-e225-4bbe-ac6f-df940f89a763"
#     },
#     "referringAgency": {
#       "name": "Kramer and Sons",
#       "email": "smccarthy@wallace-williams.org",
#       "partnerCode": "fa5e7d19-8d42-4e77-bdaa-a56b91acb221"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1989-05-22T21:54:20.759493",
#     "leaseStartDate": "2025-08-31",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Melissa",
#       "secondName": "Campbell",
#       "email": "wrightcharles@example.org",
#       "mobile": "419-786-2286"
#     },
#     "address": {
#       "text": "944 Mejia Mount Apt. 724\nNorth Nicholas, WI 71111",
#       "unit": "29",
#       "streetNumber": "15",
#       "streetName": "Johnny Throughway",
#       "locality": "North Steven",
#       "postCode": 7945,
#       "state": "Kentucky",
#       "city": "East Alanview",
#       "country": "Iraq"
#     },
#     "referringAgent": {
#       "name": "John Green",
#       "email": "julianjohnson@example.com",
#       "partnerCode": "6a109a6e-39b2-4746-8943-8b21155c375e"
#     },
#     "referringAgency": {
#       "name": "Cooke Ltd",
#       "email": "sarah44@taylor-jones.com",
#       "partnerCode": "144a2f7d-9c35-4e59-aab3-de532b2b36dc"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2010-04-22T09:18:06.594598",
#     "leaseStartDate": "2025-09-20",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jonathan",
#       "secondName": "Kim",
#       "email": "patriciaolson@example.org",
#       "mobile": "+1-334-724-8460x125"
#     },
#     "address": {
#       "text": "81624 Gregory Passage\nEast Kristen, MS 90717",
#       "unit": "47",
#       "streetNumber": "296",
#       "streetName": "Robbins Vista",
#       "locality": "East Richardland",
#       "postCode": 4987,
#       "state": "Colorado",
#       "city": "North Kimberlymouth",
#       "country": "Latvia"
#     },
#     "referringAgent": {
#       "name": "Sandra Ward",
#       "email": "warrensteven@example.net",
#       "partnerCode": "701bd7ef-aac7-47b0-843e-469b7505b7bf"
#     },
#     "referringAgency": {
#       "name": "Barber-Gonzalez",
#       "email": "ronaldabbott@robinson-becker.biz",
#       "partnerCode": "a0bd9b40-26bd-4701-b1eb-56cd94a59c68"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1998-06-28T23:36:48.491382",
#     "leaseStartDate": "2025-10-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Rita",
#       "secondName": "White",
#       "email": "ingramamy@example.org",
#       "mobile": "(925)995-7689x8008"
#     },
#     "address": {
#       "text": "1633 Diane Flat Apt. 787\nEast Juan, VT 40020",
#       "unit": "42",
#       "streetNumber": "92",
#       "streetName": "Galloway Ridges",
#       "locality": "Lake Erica",
#       "postCode": 6783,
#       "state": "Oregon",
#       "city": "West Brent",
#       "country": "Guadeloupe"
#     },
#     "referringAgent": {
#       "name": "Kyle Ramirez",
#       "email": "romerolaurie@example.org",
#       "partnerCode": "8ef763b5-61a2-4b1e-9b4e-10ed93c26f8b"
#     },
#     "referringAgency": {
#       "name": "Henderson-Dunn",
#       "email": "jennifer94@kidd-west.com",
#       "partnerCode": "5f55bd8a-1a7c-4164-a6f1-5ffa19d7d541"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2011-09-19T17:40:05.008739",
#     "leaseStartDate": "2025-11-29",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Dawn",
#       "secondName": "Gonzalez",
#       "email": "zpatel@example.com",
#       "mobile": "+1-458-409-4833"
#     },
#     "address": {
#       "text": "084 Stephanie Gateway\nGregoryfort, MN 98243",
#       "unit": "3",
#       "streetNumber": "215",
#       "streetName": "Alvarez Lodge",
#       "locality": "East Annaville",
#       "postCode": 2075,
#       "state": "Georgia",
#       "city": "Vasquezburgh",
#       "country": "Nigeria"
#     },
#     "referringAgent": {
#       "name": "Allen Sherman",
#       "email": "earl97@example.org",
#       "partnerCode": "455c67b3-afc8-4703-a45e-52182cc0de04"
#     },
#     "referringAgency": {
#       "name": "Cox-Anthony",
#       "email": "khowe@george.info",
#       "partnerCode": "ff8abb9d-b862-47fe-8f60-097c5d9051f8"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1992-07-11T12:35:18.221878",
#     "leaseStartDate": "2025-06-25",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Olivia",
#       "secondName": "Mcdonald",
#       "email": "crystalcortez@example.net",
#       "mobile": "(410)770-0973x0465"
#     },
#     "address": {
#       "text": "PSC 8891, Box 3402\nAPO AE 75686",
#       "unit": "10",
#       "streetNumber": "7",
#       "streetName": "Jill Tunnel",
#       "locality": "East Ronnie",
#       "postCode": 7955,
#       "state": "Arizona",
#       "city": "New Alexisville",
#       "country": "Palau"
#     },
#     "referringAgent": {
#       "name": "Matthew Ware",
#       "email": "nle@example.org",
#       "partnerCode": "5afc41d1-2139-477f-990f-7bf7864a159a"
#     },
#     "referringAgency": {
#       "name": "Suarez-Brown",
#       "email": "collin14@mccoy.com",
#       "partnerCode": "45c23789-773b-4dee-b566-327a5c371f7c"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1991-12-02T09:57:19.883606",
#     "leaseStartDate": "2025-12-11",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Kelly",
#       "secondName": "Robbins",
#       "email": "jamessmith@example.org",
#       "mobile": "288.619.3076x054"
#     },
#     "address": {
#       "text": "395 Jennifer Rue\nPetersmouth, GA 42706",
#       "unit": "6",
#       "streetNumber": "188",
#       "streetName": "Jerry Skyway",
#       "locality": "North Julie",
#       "postCode": 8982,
#       "state": "Vermont",
#       "city": "Hoview",
#       "country": "Bangladesh"
#     },
#     "referringAgent": {
#       "name": "Julie Gray",
#       "email": "ericewing@example.net",
#       "partnerCode": "9ec634b0-cf87-48ef-9726-200ef3a1a2a8"
#     },
#     "referringAgency": {
#       "name": "Moore-Gomez",
#       "email": "shannonknight@williams.com",
#       "partnerCode": "f90dff83-c63a-465d-888b-ce65f1fdb98a"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2020-02-03T06:51:06.865403",
#     "leaseStartDate": "2025-12-02",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Crystal",
#       "secondName": "Dodson",
#       "email": "floreselizabeth@example.net",
#       "mobile": "322.222.3461"
#     },
#     "address": {
#       "text": "692 Thornton Islands\nCarrton, GU 62678",
#       "unit": "19",
#       "streetNumber": "115",
#       "streetName": "Morales Harbor",
#       "locality": "Loriville",
#       "postCode": 5193,
#       "state": "Nevada",
#       "city": "West Deborah",
#       "country": "Heard Island and McDonald Islands"
#     },
#     "referringAgent": {
#       "name": "Erica Tyler",
#       "email": "ihensley@example.net",
#       "partnerCode": "c17ea5bc-9eab-4593-83e4-8d29b98aba7f"
#     },
#     "referringAgency": {
#       "name": "Henry-Richardson",
#       "email": "wayne85@pierce.org",
#       "partnerCode": "96901151-69fe-443e-b9a1-f41b4adf30f7"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1997-01-05T08:59:46.347543",
#     "leaseStartDate": "2026-02-26",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Wesley",
#       "secondName": "Patterson",
#       "email": "dustinbrown@example.com",
#       "mobile": "(560)574-5376"
#     },
#     "address": {
#       "text": "063 Williams Crescent Suite 880\nGrimestown, CT 12717",
#       "unit": "36",
#       "streetNumber": "381",
#       "streetName": "Griffin Bypass",
#       "locality": "Brandonmouth",
#       "postCode": 9667,
#       "state": "Wisconsin",
#       "city": "Michaelberg",
#       "country": "Aruba"
#     },
#     "referringAgent": {
#       "name": "Juan Miller",
#       "email": "robert05@example.org",
#       "partnerCode": "5565341a-e8a0-42ff-a630-81b105fa54f6"
#     },
#     "referringAgency": {
#       "name": "Hamilton-Harvey",
#       "email": "vincent74@gray.net",
#       "partnerCode": "2c1e258a-7e68-4e4c-b199-b24b355a8204"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1980-03-01T11:38:14.354145",
#     "leaseStartDate": "2025-07-22",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Justin",
#       "secondName": "Hester",
#       "email": "harrelljeffrey@example.com",
#       "mobile": "(283)851-8544x0724"
#     },
#     "address": {
#       "text": "753 Donald Plaza Suite 029\nMooreberg, IN 27044",
#       "unit": "10",
#       "streetNumber": "180",
#       "streetName": "Anna Points",
#       "locality": "East Michael",
#       "postCode": 5750,
#       "state": "Wisconsin",
#       "city": "New Lindsay",
#       "country": "Libyan Arab Jamahiriya"
#     },
#     "referringAgent": {
#       "name": "Paige Lin",
#       "email": "shannon01@example.com",
#       "partnerCode": "a4a0bc89-e1d6-493a-905e-0d82bc782f42"
#     },
#     "referringAgency": {
#       "name": "Gonzalez PLC",
#       "email": "ashleygallegos@torres-watkins.net",
#       "partnerCode": "1feaba1b-d5b5-46e1-8811-17064ca2680b"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1993-04-13T04:56:35.625084",
#     "leaseStartDate": "2026-01-09",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Shaun",
#       "secondName": "Bowen",
#       "email": "melissashaw@example.net",
#       "mobile": "5535413647"
#     },
#     "address": {
#       "text": "USNV Martinez\nFPO AP 26312",
#       "unit": "45",
#       "streetNumber": "375",
#       "streetName": "Jones Ways",
#       "locality": "Port Meganland",
#       "postCode": 6141,
#       "state": "Missouri",
#       "city": "New Heatherchester",
#       "country": "Heard Island and McDonald Islands"
#     },
#     "referringAgent": {
#       "name": "Lisa Martin",
#       "email": "michaelwillis@example.net",
#       "partnerCode": "01e7a632-1780-451c-9061-faedc6a0a155"
#     },
#     "referringAgency": {
#       "name": "Taylor-Monroe",
#       "email": "stevenschristina@kelly.biz",
#       "partnerCode": "433f8f9c-9c83-4645-8c25-801d22d38d48"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1998-02-21T17:28:30.000122",
#     "leaseStartDate": "2025-03-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Mark",
#       "secondName": "Mann",
#       "email": "elizabeth39@example.net",
#       "mobile": "359.990.8034x5231"
#     },
#     "address": {
#       "text": "76103 Montgomery Tunnel Apt. 345\nSamueltown, VI 33090",
#       "unit": "24",
#       "streetNumber": "381",
#       "streetName": "Lambert Village",
#       "locality": "South Rebeccaville",
#       "postCode": 7670,
#       "state": "New Mexico",
#       "city": "Edwinfurt",
#       "country": "Thailand"
#     },
#     "referringAgent": {
#       "name": "Whitney Lopez",
#       "email": "uphelps@example.com",
#       "partnerCode": "65cfa681-f5eb-4fc6-b030-1f2e18d69c07"
#     },
#     "referringAgency": {
#       "name": "Ryan, Thomas and Mahoney",
#       "email": "stuartrichard@thornton.net",
#       "partnerCode": "2963c597-3d9e-4bc6-be8e-8d30af8ab59a"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2009-07-28T06:13:12.562531",
#     "leaseStartDate": "2025-04-29",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Anita",
#       "secondName": "Miller",
#       "email": "davidchan@example.com",
#       "mobile": "+1-665-808-6265x904"
#     },
#     "address": {
#       "text": "691 Esparza Ways\nDebraside, VT 84423",
#       "unit": "5",
#       "streetNumber": "53",
#       "streetName": "James Mall",
#       "locality": "Shannonburgh",
#       "postCode": 6484,
#       "state": "California",
#       "city": "West Katrina",
#       "country": "Cambodia"
#     },
#     "referringAgent": {
#       "name": "Nathan Mcguire",
#       "email": "thomasnicole@example.net",
#       "partnerCode": "c6863d0f-bc1b-4ccd-9de6-70d56305f7ff"
#     },
#     "referringAgency": {
#       "name": "Carter Group",
#       "email": "bgarcia@russell.com",
#       "partnerCode": "3589e614-4b2f-469a-bde9-9fb0947d9d3a"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "2006-09-15T11:00:13.857797",
#     "leaseStartDate": "2025-05-18",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jerry",
#       "secondName": "Park",
#       "email": "teresa30@example.net",
#       "mobile": "(921)521-5559x44043"
#     },
#     "address": {
#       "text": "1064 Petersen Dale Suite 889\nSouth Maria, MA 92805",
#       "unit": "9",
#       "streetNumber": "253",
#       "streetName": "Oneill Oval",
#       "locality": "Amandastad",
#       "postCode": 3871,
#       "state": "Rhode Island",
#       "city": "Warrenborough",
#       "country": "China"
#     },
#     "referringAgent": {
#       "name": "Christine Potter",
#       "email": "michaelwilliams@example.com",
#       "partnerCode": "d4daae3f-fa0a-4055-8993-eb4b1a9918ac"
#     },
#     "referringAgency": {
#       "name": "Herrera Inc",
#       "email": "nancy42@holloway.com",
#       "partnerCode": "bb4ae5b7-5f64-4496-9f98-e8c6f72a6d3c"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "1999-12-08T22:12:01.488312",
#     "leaseStartDate": "2025-04-17",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Hannah",
#       "secondName": "Mcdowell",
#       "email": "rachel71@example.org",
#       "mobile": "(972)958-3515"
#     },
#     "address": {
#       "text": "0072 Medina Bypass Suite 587\nNew Heatherview, LA 67825",
#       "unit": "30",
#       "streetNumber": "342",
#       "streetName": "Adam Fields",
#       "locality": "New Jasmine",
#       "postCode": 2867,
#       "state": "New Mexico",
#       "city": "North Courtneytown",
#       "country": "Mongolia"
#     },
#     "referringAgent": {
#       "name": "Raymond Walsh",
#       "email": "wilcoxhunter@example.com",
#       "partnerCode": "efd24089-4036-4c8c-babf-4244563b89de"
#     },
#     "referringAgency": {
#       "name": "Bailey, Horton and Gould",
#       "email": "susanmoore@holland.info",
#       "partnerCode": "49d11c33-51fe-42f3-8c84-83e00f92ba22"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2022-09-28T16:06:50.989635",
#     "leaseStartDate": "2025-11-20",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Scott",
#       "secondName": "Wilson",
#       "email": "andersonalan@example.org",
#       "mobile": "770.564.7912x5049"
#     },
#     "address": {
#       "text": "3638 James Island Suite 000\nMorenohaven, MT 84942",
#       "unit": "48",
#       "streetNumber": "274",
#       "streetName": "Gregory Flat",
#       "locality": "Port Ruthfurt",
#       "postCode": 8000,
#       "state": "New Hampshire",
#       "city": "Castromouth",
#       "country": "Liechtenstein"
#     },
#     "referringAgent": {
#       "name": "James Bennett",
#       "email": "scottrodriguez@example.com",
#       "partnerCode": "8d922daa-48e2-425a-b71b-37ea798038f5"
#     },
#     "referringAgency": {
#       "name": "Garcia-Bell",
#       "email": "williamssabrina@hall.com",
#       "partnerCode": "c3c9ef0b-cfa8-4804-b165-979d448e325e"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2010-11-30T21:05:38.122468",
#     "leaseStartDate": "2026-01-19",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Jessica",
#       "secondName": "Orozco",
#       "email": "bwright@example.com",
#       "mobile": "001-333-243-1752x293"
#     },
#     "address": {
#       "text": "250 Navarro Port\nHeatherport, DE 18837",
#       "unit": "19",
#       "streetNumber": "485",
#       "streetName": "Jacob Fort",
#       "locality": "New Andreafort",
#       "postCode": 7468,
#       "state": "South Dakota",
#       "city": "North Martin",
#       "country": "South Georgia and the South Sandwich Islands"
#     },
#     "referringAgent": {
#       "name": "Peter Mcintyre",
#       "email": "kimberlyweber@example.net",
#       "partnerCode": "910e94db-4daf-4b22-bd8d-d45fe9c7541e"
#     },
#     "referringAgency": {
#       "name": "Baker and Sons",
#       "email": "brittany70@martin.com",
#       "partnerCode": "8f6d888f-46c1-4cf8-ba4e-8b9bbc67f0ca"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1972-01-14T23:30:06.926553",
#     "leaseStartDate": "2025-05-02",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "David",
#       "secondName": "Salazar",
#       "email": "summer52@example.com",
#       "mobile": "001-989-473-2340x686"
#     },
#     "address": {
#       "text": "778 Victoria Rue\nEllisborough, CO 08946",
#       "unit": "28",
#       "streetNumber": "175",
#       "streetName": "Hutchinson Center",
#       "locality": "Robersonborough",
#       "postCode": 1522,
#       "state": "Vermont",
#       "city": "New Julie",
#       "country": "Faroe Islands"
#     },
#     "referringAgent": {
#       "name": "Cindy Soto",
#       "email": "lisaroberts@example.org",
#       "partnerCode": "613705ed-aa03-4e89-a658-0674c991a3da"
#     },
#     "referringAgency": {
#       "name": "Morrow Ltd",
#       "email": "dsloan@bowen.org",
#       "partnerCode": "31ad97dd-2c6a-43c1-9308-b2dd8b32e105"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1970-11-15T19:42:31.033816",
#     "leaseStartDate": "2025-03-16",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Deborah",
#       "secondName": "Wyatt",
#       "email": "smallchristopher@example.net",
#       "mobile": "546-854-2678x700"
#     },
#     "address": {
#       "text": "38365 Cheryl Forge\nWest Sherry, WA 03473",
#       "unit": "19",
#       "streetNumber": "267",
#       "streetName": "Monique Mount",
#       "locality": "Susanbury",
#       "postCode": 1647,
#       "state": "Florida",
#       "city": "North Cathy",
#       "country": "Tonga"
#     },
#     "referringAgent": {
#       "name": "Erik Rivera",
#       "email": "holmesnancy@example.org",
#       "partnerCode": "b135a62b-1650-4334-a7ae-c3328dbc0e86"
#     },
#     "referringAgency": {
#       "name": "Goodman, Pierce and Williams",
#       "email": "kimberlymendoza@rodriguez.com",
#       "partnerCode": "b24f17e3-51da-4489-a1e0-1ffb84f41149"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1991-02-02T17:54:54.540670",
#     "leaseStartDate": "2025-09-09",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Lucas",
#       "secondName": "Newton",
#       "email": "jessica47@example.net",
#       "mobile": "819.793.5832x406"
#     },
#     "address": {
#       "text": "85666 Powers Fort\nNew Jenniferburgh, ME 58834",
#       "unit": "31",
#       "streetNumber": "43",
#       "streetName": "Mccann Vista",
#       "locality": "Lake Jennifer",
#       "postCode": 9298,
#       "state": "Wyoming",
#       "city": "Stevenston",
#       "country": "Congo"
#     },
#     "referringAgent": {
#       "name": "Benjamin Stephens",
#       "email": "cherylsuarez@example.com",
#       "partnerCode": "494c12fb-2693-40ba-8e17-c1ebc6f7eb22"
#     },
#     "referringAgency": {
#       "name": "Parker, Richardson and Le",
#       "email": "gcross@wilson-simpson.com",
#       "partnerCode": "15c64179-0f40-45f5-8dc3-4138609523dd"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1998-04-01T13:30:22.619660",
#     "leaseStartDate": "2025-10-03",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Francisco",
#       "secondName": "Valdez",
#       "email": "fosterdaniel@example.net",
#       "mobile": "(779)336-6135x47582"
#     },
#     "address": {
#       "text": "7961 Mcclure Underpass Suite 389\nTiffanymouth, AZ 96346",
#       "unit": "21",
#       "streetNumber": "93",
#       "streetName": "Melissa Landing",
#       "locality": "Kirbytown",
#       "postCode": 5905,
#       "state": "Nevada",
#       "city": "New Christina",
#       "country": "Holy See (Vatican City State)"
#     },
#     "referringAgent": {
#       "name": "Christopher Salas",
#       "email": "martinjoseph@example.com",
#       "partnerCode": "5155077b-09bb-4a21-bcf2-aa4fae886471"
#     },
#     "referringAgency": {
#       "name": "Wade-Williams",
#       "email": "kristie57@adams.biz",
#       "partnerCode": "40bae103-5c72-46b4-a817-e365d44bc44d"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2015-07-09T17:20:30.572437",
#     "leaseStartDate": "2026-01-08",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Vicki",
#       "secondName": "Koch",
#       "email": "moorejohn@example.net",
#       "mobile": "001-987-552-3643x610"
#     },
#     "address": {
#       "text": "2292 Miller Lights\nJohnfurt, NC 76337",
#       "unit": "22",
#       "streetNumber": "465",
#       "streetName": "Johnston Ramp",
#       "locality": "Ginaborough",
#       "postCode": 7237,
#       "state": "Montana",
#       "city": "New Susan",
#       "country": "Somalia"
#     },
#     "referringAgent": {
#       "name": "Charles Lawrence IV",
#       "email": "lanekathy@example.com",
#       "partnerCode": "99779364-2b55-4250-96a6-59ecbc5048dd"
#     },
#     "referringAgency": {
#       "name": "Diaz-Bowen",
#       "email": "peggyhernandez@huerta-dillon.org",
#       "partnerCode": "bcc2d369-b53b-413a-9f05-6ec3ebc8f03c"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1999-10-01T14:07:24.571132",
#     "leaseStartDate": "2025-11-30",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Francisco",
#       "secondName": "Friedman",
#       "email": "yhowell@example.com",
#       "mobile": "657-609-3574x651"
#     },
#     "address": {
#       "text": "106 Melanie Mountain Apt. 333\nNorth Molly, VI 98718",
#       "unit": "27",
#       "streetNumber": "53",
#       "streetName": "Austin Freeway",
#       "locality": "Lake Ronaldborough",
#       "postCode": 3734,
#       "state": "Ohio",
#       "city": "Campbellfurt",
#       "country": "Barbados"
#     },
#     "referringAgent": {
#       "name": "Michael Andrews",
#       "email": "patricia38@example.com",
#       "partnerCode": "758e88af-3e6f-471a-bf2c-0bec139d8c83"
#     },
#     "referringAgency": {
#       "name": "Martin-Anderson",
#       "email": "kristineconley@smith.com",
#       "partnerCode": "73404eaa-1726-440b-b520-5e678581db9e"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": True
#     },
#     "submitted": "2011-01-22T12:17:54.942857",
#     "leaseStartDate": "2025-11-14",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Maria",
#       "secondName": "Mejia",
#       "email": "diana05@example.org",
#       "mobile": "(391)698-7684x505"
#     },
#     "address": {
#       "text": "974 Chad Mountains Apt. 556\nChristinefort, NC 13976",
#       "unit": "3",
#       "streetNumber": "273",
#       "streetName": "Sean Underpass",
#       "locality": "Ortizstad",
#       "postCode": 6901,
#       "state": "New York",
#       "city": "Philipview",
#       "country": "Suriname"
#     },
#     "referringAgent": {
#       "name": "Thomas Meyer",
#       "email": "omorales@example.org",
#       "partnerCode": "19d3e770-8174-4244-8ba5-bcfe03d14bfb"
#     },
#     "referringAgency": {
#       "name": "Fisher, Mccarthy and Young",
#       "email": "davisjoyce@austin.org",
#       "partnerCode": "a72f1dec-c0e6-4752-93e8-fee2734c0091"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": True
#     },
#     "submitted": "1992-10-20T07:13:10.257525",
#     "leaseStartDate": "2026-02-19",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Christopher",
#       "secondName": "Fisher",
#       "email": "jeremy27@example.com",
#       "mobile": "+1-223-491-3458"
#     },
#     "address": {
#       "text": "8834 Mcdonald Parks\nSouth Christopher, PA 19539",
#       "unit": "19",
#       "streetNumber": "492",
#       "streetName": "Mckinney Estates",
#       "locality": "Swansonshire",
#       "postCode": 8926,
#       "state": "Wisconsin",
#       "city": "Wrightstad",
#       "country": "Tajikistan"
#     },
#     "referringAgent": {
#       "name": "Brian Hunt",
#       "email": "joshuahenson@example.net",
#       "partnerCode": "0dadd574-33cf-4a32-96bb-d4201ecd3f28"
#     },
#     "referringAgency": {
#       "name": "Ruiz-Hunt",
#       "email": "williamskathleen@horton-green.com",
#       "partnerCode": "d6410e51-9f57-4776-ac7d-e19b360d7088"
#     },
#     "services": {
#       "gas": True,
#       "electricity": False,
#       "internet": True,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1971-08-09T22:58:06.090128",
#     "leaseStartDate": "2025-05-13",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Denise",
#       "secondName": "Aguilar",
#       "email": "williamadams@example.org",
#       "mobile": "330.638.3260"
#     },
#     "address": {
#       "text": "3780 Erickson Villages\nSouth Andrea, AR 25241",
#       "unit": "24",
#       "streetNumber": "161",
#       "streetName": "James Harbors",
#       "locality": "East Timothyport",
#       "postCode": 8336,
#       "state": "Nebraska",
#       "city": "East Angelahaven",
#       "country": "Equatorial Guinea"
#     },
#     "referringAgent": {
#       "name": "Daniel Mitchell Jr.",
#       "email": "leonjennifer@example.net",
#       "partnerCode": "50c0e282-6a21-42bf-ac5e-9fcec7bc5c21"
#     },
#     "referringAgency": {
#       "name": "Hayes LLC",
#       "email": "jeremy44@stafford-robinson.com",
#       "partnerCode": "0db39aea-1cf5-42bd-87ef-389cef51047a"
#     },
#     "services": {
#       "gas": False,
#       "electricity": False,
#       "internet": False,
#       "telephone": False,
#       "payTV": True,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1990-10-25T11:10:47.103784",
#     "leaseStartDate": "2025-10-08",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Nicole",
#       "secondName": "Ortiz",
#       "email": "jessica10@example.org",
#       "mobile": "456.220.0747x98667"
#     },
#     "address": {
#       "text": "9456 Zuniga Field\nPort Joseview, MH 48814",
#       "unit": "49",
#       "streetNumber": "247",
#       "streetName": "Walters Roads",
#       "locality": "South Travis",
#       "postCode": 7551,
#       "state": "Alaska",
#       "city": "Port Kimberly",
#       "country": "Namibia"
#     },
#     "referringAgent": {
#       "name": "Kathleen Jones",
#       "email": "jessicamartinez@example.com",
#       "partnerCode": "d94e4b30-9360-43c3-a91f-5bdc66894540"
#     },
#     "referringAgency": {
#       "name": "Wilson PLC",
#       "email": "jamesduncan@hoffman.com",
#       "partnerCode": "4cbdbf44-af1d-428f-90bd-fded86354309"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": False,
#       "telephone": False,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": False,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "1972-05-23T17:51:31.897604",
#     "leaseStartDate": "2025-12-21",
#     "renewal": True
#   },
#   {
#     "tenant": {
#       "firstName": "Adam",
#       "secondName": "Ashley",
#       "email": "roselawson@example.org",
#       "mobile": "769-479-7103x20242"
#     },
#     "address": {
#       "text": "PSC 5379, Box 4237\nAPO AE 92343",
#       "unit": "41",
#       "streetNumber": "82",
#       "streetName": "Dennis Circle",
#       "locality": "Lucasmouth",
#       "postCode": 5076,
#       "state": "Maine",
#       "city": "Port Tiffany",
#       "country": "Saint Martin"
#     },
#     "referringAgent": {
#       "name": "Christopher Williams",
#       "email": "stricklandsamantha@example.com",
#       "partnerCode": "73dc3a81-df49-4aa6-826d-13d6f7785da6"
#     },
#     "referringAgency": {
#       "name": "Gonzalez, Kelly and Gillespie",
#       "email": "vlane@robertson.info",
#       "partnerCode": "fcdb4aee-7bb1-4a84-8be1-fa28e7113fd9"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": False,
#       "cleaning": True,
#       "removalist": True,
#       "movingBoxes": True,
#       "vehicleHire": False,
#       "water": False
#     },
#     "submitted": "2015-09-05T15:17:12.901145",
#     "leaseStartDate": "2025-08-12",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "David",
#       "secondName": "Montgomery",
#       "email": "austinbrandy@example.org",
#       "mobile": "719.638.3493"
#     },
#     "address": {
#       "text": "25954 Clark Squares\nRachelfort, WY 61220",
#       "unit": "50",
#       "streetNumber": "259",
#       "streetName": "Nolan Divide",
#       "locality": "Simmonsland",
#       "postCode": 4865,
#       "state": "South Carolina",
#       "city": "North Monica",
#       "country": "Cayman Islands"
#     },
#     "referringAgent": {
#       "name": "Melissa Williams",
#       "email": "johnsonteresa@example.com",
#       "partnerCode": "4b3589a1-b04f-46d7-bf98-13cb79ef522f"
#     },
#     "referringAgency": {
#       "name": "Bailey, Harding and Bryant",
#       "email": "melody71@krueger.com",
#       "partnerCode": "1c7d9442-4370-4613-bf95-00892eef003c"
#     },
#     "services": {
#       "gas": True,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": False,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "2015-08-16T15:08:53.452988",
#     "leaseStartDate": "2025-10-19",
#     "renewal": False
#   },
#   {
#     "tenant": {
#       "firstName": "Amanda",
#       "secondName": "Ellis",
#       "email": "crawfordnicole@example.org",
#       "mobile": "9303922061"
#     },
#     "address": {
#       "text": "07218 Diane Ports Suite 360\nMichaelchester, RI 91670",
#       "unit": "11",
#       "streetNumber": "304",
#       "streetName": "Lori Throughway",
#       "locality": "Port Jason",
#       "postCode": 7304,
#       "state": "Wyoming",
#       "city": "New Walter",
#       "country": "Bouvet Island (Bouvetoya)"
#     },
#     "referringAgent": {
#       "name": "Vanessa Barry",
#       "email": "kristin81@example.net",
#       "partnerCode": "8f818ef0-05b6-464c-a510-03895fb94d6e"
#     },
#     "referringAgency": {
#       "name": "Wilkinson Group",
#       "email": "burkericky@johnson.com",
#       "partnerCode": "0c280cc7-008e-4f15-8bb3-49c2f11eff57"
#     },
#     "services": {
#       "gas": False,
#       "electricity": True,
#       "internet": True,
#       "telephone": True,
#       "payTV": True,
#       "cleaning": False,
#       "removalist": False,
#       "movingBoxes": True,
#       "vehicleHire": True,
#       "water": False
#     },
#     "submitted": "1973-06-06T23:39:00.860261",
#     "leaseStartDate": "2025-09-15",
#     "renewal": True
#   }
# ]
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

def get_flk_leads_from_db(page_number=1, items_per_page=10, filter_date=None):
    """
    Fetch paginated leads from the database with an optional date filter.

    :param page_number: The page number for pagination.
    :param items_per_page: The number of items per page.
    :param filter_date: Optional date to filter leads by submitted_date (format: 'YYYY-MM-DD').
    :return: Paginated leads
    """
    # Filtering based on the submitted date if provided
    if filter_date:
        # Parse the date string into a datetime object
        filter_date = datetime.strptime(filter_date, "%Y-%m-%d")

        # Fetch leads filtered by submitted_date greater than or equal to the filter date
        leads_queryset = Flk_lead.objects.filter(submitted_date__gte=filter_date)
    else:
        # If no date filter is applied, fetch all leads
        leads_queryset = Flk_lead.objects.all()

    # Set up pagination
    paginator = Paginator(leads_queryset, items_per_page)  # Paginate the queryset

    # Get the page of leads based on the page_number
    page = paginator.get_page(page_number)
    
    has_more_data = page.has_next()

    # Prepare the result to return
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
    leads_ = get_flk_leads_from_db(page_number=page)
    return Response(leads_)
    