from rest_framework import serializers
from .models import Address

class AddressSerializers(serializers.Serializer):
    class Meta:
        model = Address
        fields = ['name','phoneNumber', 'address', 'created']

