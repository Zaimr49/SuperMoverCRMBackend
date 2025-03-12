from django.db import models

# Create your models here.

class SignUp(models.Model):
    """
    Stores the data from the multi-step sign-up form.
    """

    # Step 1 fields
    connection_type = models.CharField(max_length=50, blank=True)  # "moveIn" or "transfer"
    products = models.JSONField(default=list)  # e.g. ["electricity","gas"] 
    customer_type = models.CharField(max_length=50, blank=True)    # "residential" or "business"

    # Step 2 fields
    title = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    best_contact_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    physical_address = models.CharField(max_length=255, blank=True)
    is_billing_same_as_physical = models.BooleanField(null=True, blank=True)
    billing_address = models.CharField(max_length=255, blank=True)
    how_did_you_hear = models.CharField(max_length=100, blank=True)

    # Step 3 fields
    is_owner = models.BooleanField(null=True, blank=True)
    has_solar = models.BooleanField(null=True, blank=True)

    # Step 4 fields
    dob = models.CharField(max_length=20, blank=True)  # or DateField if you prefer
    verification_method = models.CharField(max_length=50, blank=True)  # e.g. "Driver's License"
    id_number = models.CharField(max_length=100, blank=True)
    id_expiry = models.CharField(max_length=20, blank=True)  # or DateField
    home_phone = models.CharField(max_length=50, blank=True)
    mobile_phone = models.CharField(max_length=50, blank=True)
    confirm_email = models.EmailField(blank=True)

    # Step 5 fields
    wants_secondary_contact = models.BooleanField(null=True, blank=True)
    secondary_title = models.CharField(max_length=20, blank=True)
    secondary_first_name = models.CharField(max_length=100, blank=True)
    secondary_last_name = models.CharField(max_length=100, blank=True)
    secondary_mobile = models.CharField(max_length=50, blank=True)
    secondary_home_phone = models.CharField(max_length=50, blank=True)
    secondary_email = models.EmailField(blank=True)

    # Step 6 fields
    move_in_date = models.DateTimeField(null=True, blank=True)  # or DateField
    has_been_disconnected12months = models.BooleanField(null=True, blank=True)
    has_building_electrical_works = models.BooleanField(null=True, blank=True)
    has_clear_meter_access = models.BooleanField(null=True, blank=True)

    # Step 7 fields
    life_support = models.BooleanField(null=True, blank=True)
    is_concession_holder = models.BooleanField(null=True, blank=True)
    concession_type = models.CharField(max_length=100, blank=True)
    concession_card_number = models.CharField(max_length=50, blank=True)
    concession_card_start_date = models.CharField(max_length=20, blank=True)
    concession_card_expiry_date = models.CharField(max_length=20, blank=True)

    # Step 8 fields
    medical_cooling_concession = models.BooleanField(null=True, blank=True)
    concessioner_declaration_provided = models.BooleanField(null=True, blank=True)

    # Step 9 fields
    consent_electronic_bills = models.BooleanField(null=True, blank=True)
    all_communication_same_method = models.BooleanField(null=True, blank=True)
    use_primary_email_for_all = models.BooleanField(null=True, blank=True)
    is_postal_address_correct = models.BooleanField(null=True, blank=True)

    # Step 10 fields
    monthly_bills_ok = models.BooleanField(null=True, blank=True)
    promotional_contact_consent = models.BooleanField(null=True, blank=True)

    # Step 11 fields
    has_reviewed_market_offer_summary = models.BooleanField(null=True, blank=True)
    has_reviewed_eic_script = models.BooleanField(null=True, blank=True)

    # Final submission doesn't have extra fields, but you can add timestamps:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SignUp: {self.first_name} {self.last_name} - {self.connection_type}"
