# myapp/views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .models import User
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import CustomUser
from .forms import RegisterForm


        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful", "token": user.token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response(serializer.data)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            
            # Generate OTP
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.is_active = False
            user.save()

            # Send email
            send_mail(
                subject='Your OTP Verification Code',
                message=f'Your OTP code is {otp}',
                from_email='yourgmail@gmail.com',
                recipient_list=[user.email],
            )

            messages.success(request, 'OTP sent to your email.')
            return redirect('verify_otp', user_id=user.id)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def verify_otp_view(request, user_id):
    if request.method == "POST":
        otp_entered = request.POST.get('otp')
        user = CustomUser.objects.get(id=user_id)

        if user.otp == otp_entered:
            user.is_active = True
            user.is_verified = True
            user.otp = ''
            user.save()
            messages.success(request, 'Your account has been verified!')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP, please try again.')

    return render(request, 'verify_otp.html')
