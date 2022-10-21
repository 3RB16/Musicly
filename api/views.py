from msilib.schema import AppId
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import RoomModel
from .serializers import RoomSerializer

class RoomView(APIView):
    def get(self , request):
        serializer_class = RoomSerializer(RoomModel.objects.all() , many = True)
        return Response(serializer_class.data , status = status.HTTP_200_OK)