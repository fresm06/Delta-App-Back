from rest_framework import serializers
from .models import UploadedFile, Delta

class DeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delta
        fields = ['title', 'picture', 'detail', 'idea', 'studyTime']

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file', 'uploaded_on')