from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers.user_serializer import UserSerializer

class UserView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

