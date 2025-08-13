# myapp/views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully", "token": user.token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful", "token": user.token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
