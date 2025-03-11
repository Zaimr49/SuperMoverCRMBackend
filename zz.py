import requests
from datetime import datetime

# # API URL
# url = "https://api.flkitover.com/v2/leads?submitted=2025-01-01"
submitted_date = datetime(2025, 3, 10).isoformat() + "Z"
# params = {"submitted": submitted_date}
params = {"submitted": "2025-01-10"}
print(params)

url = "https://api.flkitover.com/v2/leads"

# Your Bearer Token (Replace with actual token)
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJmbGtfYzNWd1pYSnRiM1psY25WIiwic2NvcGUiOiJyZWFkLmxlYWRzIiwibWV0YSI6eyJhbGxvd2VkQ29ubmVjdGlvbkNvbXBhbmllcyI6WyI2N2I2NjYzZmM3MDJiMDJiYjg5Yzk1ZDYiXX0sImlhdCI6MTc0MTY4OTgyMSwiZXhwIjoxNzQxNjkzNDIxfQ.cpP-RXRqGb6KzlUJAhsag-LbJMDviDwysHmpCCCOmxs"

# Headers with Bearer Token
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {bearer_token}",
}

try:
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()

    if response.status_code == 200:
        print("Leads Data:", response_data)
    else:
        print("Error:", response_data)

except requests.RequestException as e:
    print("Request failed:", str(e))



# def get_flk_access_token():
#   api_base_url = "https://api.staging.flkitover.com/v2"
#   url = f"{api_base_url}/oauth/token"
#   data = {
#       "grant_type": "client_credentials",
#       "client_id": 'flk_c3VwZXJtb3ZlcnV',
#       "client_secret": ".PvUZAKXQceyATc_vqwqvyYf*qkvEff2n.-J.bwU",
#       "scope": "read.leads",
#   }
#   headers = {
#       "Accept": "application/json",
#       "Content-Type": "application/x-www-form-urlencoded",
#   }
#   response = requests.post(url, data=data, headers=headers)
#   try:
#     print(response.json())
#   except:
#     print(response.text)

# get_flk_access_token()