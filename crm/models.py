from django.db import models
from django.utils.timezone import now
from core.models import User

def default_extra():
    return {
        "connectionType": "",
        "customerType": "",
        "isOwner": None,
        "hasSolar": None,
        "dob": "",
        "verificationMethod": "",
        "idNumber": "",
        "idExpiry": "",
        "homePhone": "",
        "mobilePhone": "",
        "confirmEmail": "",
        "wantsSecondaryContact": None,
        "secondaryTitle": "",
        "secondaryFirstName": "",
        "secondaryLastName": "",
        "secondaryMobile": "",
        "secondaryHomePhone": "",
        "secondaryEmail": "",
        "hasBeenDisconnected12Months": None,
        "hasBuildingElectricalWorks": None,
        "hasClearMeterAccess": None,
        "lifeSupport": None,
        "isConcessionHolder": None,
        "concessionType": "",
        "concessionCardNumber": "",
        "concessionCardStartDate": "",
        "concessionCardExpiryDate": "",
        "medicalCoolingConcession": None,
        "concessionerDeclarationProvided": None,
        "consentElectronicBills": None,
        "allCommunicationSameMethod": None,
        "usePrimaryEmailForAll": None,
        "isPostalAddressCorrect": None,
        "monthlyBillsOk": None,
        "promotionalContactConsent": None,
        "hasReviewedMarketOfferSummary": None,
        "hasReviewedEICScript": None
    }

class Flk_lead(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('call_attempt', 'Call Attempt'),
        ('sale', 'Sale'),
        ('no_sale', 'No Sale'),
    )

    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    # Storing nested data as JSON fields
    tenant = models.JSONField()
    address = models.JSONField()
    referring_agent = models.JSONField()
    referring_agency = models.JSONField()
    services = models.JSONField()
    extra = models.JSONField(default=default_extra) #{}
    

    submitted = models.DateTimeField()
    lease_start_date = models.DateField(default=None, blank=True, null=True)
    renewal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"
