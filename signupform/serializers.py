from rest_framework import serializers
from .models import SignUp

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = '__all__'
        # or list them explicitly
        # fields = [
        #     'id', 'connection_type', 'products', 'customer_type',
        #     'title', 'first_name', 'last_name', 'best_contact_number', 'email',
        #     ...
        # ]
