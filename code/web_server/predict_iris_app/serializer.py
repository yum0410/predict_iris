from rest_framework import serializers
from .models import Iris

class IrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iris
        fields = '__all__'
