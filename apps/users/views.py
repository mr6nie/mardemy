from rest_framework import generics, status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import UserCreationSerializer

User = get_user_model()

class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




