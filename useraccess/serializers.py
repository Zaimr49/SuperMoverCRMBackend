from rest_framework import serializers
from .models import UserAccessRole

class UserAccessRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccessRole
        fields = '__all__'
