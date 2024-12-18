from rest_framework import serializers
from .models import Accounts, Destinations

# Account Serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['email_id','account_id','account_name','website']

# Destination Serializer
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'
        extra_kwargs = {
            'account': {'required': False},  # Make 'account' not required
        }