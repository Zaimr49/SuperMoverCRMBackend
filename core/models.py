from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('manager', 'Manager'),
#         ('staff', 'Staff'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')

#     def __str__(self):
#         return self.username



class User(AbstractUser):
    # Add any custom fields you need for your User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',  # Avoids clash
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions_set',  # Avoids clash
        blank=True,
        help_text='Specific permissions for this user.'
    )