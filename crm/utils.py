import requests
import time
from django.conf import settings

def get_flk_access_token():
    """Fetches a new access token if expired or not set."""
    current_time = time.time()

    # Ensure API base URL is correct
    api_base_url = getattr(settings, "FLK_STAGING_API_BASE_URL", None)
    if not api_base_url:
      raise Exception("FLK_STAGING_API_BASE_URL is not set in settings.")

    # Check if token is still valid
    if settings.FLK_ACCESS_TOKEN and settings.FLK_TOKEN_EXPIRY and current_time < settings.FLK_TOKEN_EXPIRY:
      return settings.FLK_ACCESS_TOKEN
    url = f"{api_base_url}/oauth/token"
    data = {
      "grant_type": "client_credentials",
      "client_id": settings.FLK_USERNAME,
      "client_secret": settings.FLK_PASSWORD,
      "scope": "read.leads",
    }
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
      response = requests.post(url, data=data, headers=headers)
      if response.status_code == 200:
        data = response.json()
        settings.FLK_ACCESS_TOKEN = data["access_token"]
        settings.FLK_TOKEN_EXPIRY = current_time + data["expires_in"]  # Store expiry time
        return data["access_token"]
      else:
        raise Exception(f"Failed to refresh token: {response.text}")
    except requests.RequestException as e:
        raise Exception(f"Request error while refreshing token: {str(e)}")

        
