from rest_framework import serializers
from .models import Address

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['name','phone_number', 'address', 'created']

