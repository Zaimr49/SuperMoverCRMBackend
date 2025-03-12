from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('call_attempt', 'Call Attempt'),
        ('sale', 'Sale'),
        ('no_sale', 'No Sale'),
    ]

    # Customer Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    # Address
    billing_address = models.CharField(max_length=255, blank=True)
    street_address = models.CharField(max_length=255, blank=True)
    suburb = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=100, blank=True)

    # Products
    electricity = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    broadband = models.BooleanField(default=False)

    # Move-in date
    move_in_date = models.DateField(null=True, blank=True)

    # REA Details
    rea_office = models.CharField(max_length=255, blank=True)
    referred_agent_name = models.CharField(max_length=255, blank=True)
    rea_software_used = models.CharField(max_length=255, blank=True)

    # Lead Management
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    notes = models.TextField(blank=True)  # if you want to store any extra notes

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
