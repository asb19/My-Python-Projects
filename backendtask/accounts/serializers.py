from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Favourite


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password','id'
                  ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):

        user = User.objects.create_user(username=validated_data['email'],**validated_data)
        profile=UserProfile.objects.create(user=user,first_name=validated_data['first_name'], last_name=validated_data['last_name'],email=validated_data['email'],favourites=[])
        profile.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user_id","favourites","email","first_name","last_name"]

class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ("id","category")
