from django.db import models
from core.models import User

# class Lead(models.Model):
#     STATUS_CHOICES = (
#         ('new', 'New'),
#         ('call_attempt', 'Call Attempt'),
#         ('sale', 'Sale'),
#         ('no_sale', 'No Sale'),
#     )
#     assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     customer_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
#     notes = models.TextField(blank=True)

#     def __str__(self):
#         return self.customer_name


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

    submitted = models.DateTimeField()
    lease_start_date = models.DateField()
    renewal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"

# class Sale(models.Model):
#     lead = models.OneToOneField(Lead, on_delete=models.CASCADE)
#     commission_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])
#     amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Sale for {self.lead.customer_name}"
