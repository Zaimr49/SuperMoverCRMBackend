from django.db import models
from core.models import User

class Lead(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('call_attempt', 'Call Attempt'),
        ('sale', 'Sale'),
        ('no_sale', 'No Sale'),
    )
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.customer_name

class Sale(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE)
    commission_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale for {self.lead.customer_name}"
