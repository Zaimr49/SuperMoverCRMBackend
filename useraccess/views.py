from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserAccessRole
from .serializers import UserAccessRoleSerializer

class UserAccessRoleViewSet(viewsets.ModelViewSet):
    queryset = UserAccessRole.objects.all()
    serializer_class = UserAccessRoleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            # Return dummy data if no roles exist in the database.
            dummy_data = [
                {
                    "id": 1,
                    "first_name": "John",
                    "last_name": "Smith",
                    "role": "Lead Manager",
                    "users_count": 1,
                    "last_updated": "June 5, 2023, 4:36 PM",
                    "created_by": "John Smith",
                    "phone": "123-456-7890",
                    "mobile": "987-654-3210",
                    "email": "john.smith@example.com",
                    "position": "Lead Manager",
                    "category": "Management",
                    "avatar": "https://randomuser.me/api/portraits/men/30.jpg",
                    "created_at": None
                },
                {
                    "id": 2,
                    "first_name": "Charlotte",
                    "last_name": "R.",
                    "role": "Sales Manager",
                    "users_count": 1,
                    "last_updated": "Sep 16, 2023, 3:45 PM",
                    "created_by": "Charlotte R.",
                    "phone": "123-555-7890",
                    "mobile": "987-555-3210",
                    "email": "charlotte.r@example.com",
                    "position": "Sales Manager",
                    "category": "Sales",
                    "avatar": "https://randomuser.me/api/portraits/women/31.jpg",
                    "created_at": None
                },
                # ... add additional dummy roles if desired
            ]
            return Response(dummy_data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
