from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from model.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
import pdb

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

    if not check_password(password, user.password):
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

    request.session['user_id'] = user.id

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def logout(request):
    pdb.set_trace()
    print(request.user)
    logout(request)
    return Response(status=status.HTTP_200_OK)
