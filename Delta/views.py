from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Delta
from .serializers import DeltaSerializer
import random
from rest_framework import viewsets
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .serializers import FileUploadSerializer



@api_view(['GET'])
def PostAPI(request,id):
    totalPosts = Delta.objects.all()
    randomPosts = random.sample(list(totalPosts), id)
    serializer = DeltaSerializer(randomPosts, many=True)
    return Response(serializer.data)


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    class Meta:
        db_table = 'Delta_uploadedfile'