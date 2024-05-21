from rest_framework import serializers
from .models import Delta

class DeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delta
        fields = ['title']