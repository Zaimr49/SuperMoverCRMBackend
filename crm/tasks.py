import requests
from celery import shared_task
from datetime import datetime
from django.conf import settings
from .utils import get_flk_access_token
from .models import Flk_lead

@shared_task
def flk_leads_bg_task():
    print("**********")
    print("**** RUNNING flk_leads_bg_task task......")
    print("**********")
    todayDate = datetime.now().strftime("%Y-%m-%d")
    params = {"submitted": todayDate}  # Modify as needed
    url = f"{settings.FLK_API_BASE_URL}/leads"
    access_token = get_flk_access_token()
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("** Error:", response.text)
        res_ = {
            "error": response.text
        }
        print(res_)
        return res_
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
    resp_ = {"message": "Leads stored successfully", "created_leads": created_leads}
    print(resp_)
    return resp_


@shared_task
def rea_leads_bg_task():
    print("**********")
    print("**** RUNNING flk_leads_bg_task task......")
    print("**********")
    return "Completed"
