from rest_framework import serializers
from .models import Flk_lead

class FlkLeadSerializer(serializers.ModelSerializer):
    class Meta:
      model = Flk_lead
      fields = '__all__'  # Includes all model fields
