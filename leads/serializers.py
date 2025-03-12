from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        # or list them explicitly:
        # fields = [
        #     'id', 'first_name', 'last_name', 'phone', 'email',
        #     'billing_address', 'street_address', 'suburb', 'postcode', 'state',
        #     'electricity', 'gas', 'water', 'broadband',
        #     'move_in_date',
        #     'rea_office', 'referred_agent_name', 'rea_software_used',
        #     'status', 'assigned_to', 'notes',
        #     'created_at', 'updated_at'
        # ]
