from django.db import models

# Create your models here.

class UserAccessRole(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    users_count = models.IntegerField(default=0)
    # Store the last updated date automatically
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    avatar = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} - {self.first_name} {self.last_name}"
