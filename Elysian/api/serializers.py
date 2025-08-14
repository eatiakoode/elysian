# myapp/serializers.py
from rest_framework import serializers
from .models import User
import uuid
import hashlib

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['u_name', 'email', 'password', 'dob']  # Added dob field

    def create(self, validated_data):
        # hash password before saving
        validated_data['password'] = hashlib.sha256(validated_data['password'].encode()).hexdigest()
        validated_data['token'] = str(uuid.uuid4())
        return User.objects.create(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    u_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        hashed_pw = hashlib.sha256(data['password'].encode()).hexdigest()
        try:
            user = User.objects.get(u_name=data['u_name'], password=hashed_pw)
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")
