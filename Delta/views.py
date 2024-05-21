from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Delta
from .serializers import DeltaSerializer
import random


@api_view(['GET'])
def PostAPI(request,id):
    totalPosts = Delta.objects.all()
    randomPosts = random.sample(list(totalPosts), id)
    serializer = DeltaSerializer(randomPosts, many=True)
    return Response(serializer.data)
    