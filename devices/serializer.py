from .models import shop
from rest_framework import serializers


class shopserializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'
