from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer, UserProfileSerializer, FavouritesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSerializer
    def get(self,request):
        email = request.data.get('email','')
        if User.objects.filter(email=email).exists()==False:
            return Response({"user_id":"not registered","logintype":"signup"}, status=status.HTTP_404_NOT_FOUND)
        serializer =UserSerializer(User.objects.get(email=email))
        print(serializer)
        return Response({"user_id":serializer.data['id'],"login_type":"signin"})



    def post(self, request):
        data = request.data
        userId = data.get('user_id', '')
        password = data.get('password', '')
        cuserv = User.objects.get(id=userId)
        email = cuserv.email
        user = auth.authenticate(username=email, password=password)
        print(user)

        if user:

            serializer = UserSerializer(user)

            data = {'message': "successfull"}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'message': 'Failed'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileDetailsApi(APIView):
    def get(self,request):
        id=request.data.get('user_id')
        user = User.objects.get(pk=id)
        usereProfiles = UserProfile.objects.get(email=user.email)
        serializer = UserProfileSerializer(usereProfiles)
        return Response(serializer.data)


class FavouriteAddApi(APIView):
    serializer_class = FavouritesSerializer

    def post(self,request):
        user_id = request.data.get('user_id','')
        user = User.objects.get(id=user_id)
        category = request.data.get('category','')

        userprofile = UserProfile.objects.get(email=user.email)
        userprofile.favourites.add(category)
        userprofile.save()
        return Response(userprofile)

