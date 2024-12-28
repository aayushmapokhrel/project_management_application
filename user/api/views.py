from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from user.api.serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status


class UserDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"username": user.username, "email": user.email})

    def put(self, request, *args, **kwargs):
        user = request.user
        user.first_name = request.data.get("first_name", user.first_name)
        user.last_name = request.data.get("last_name", user.last_name)
        user.email = request.data.get("email", user.email)
        user.username = request.data.get("username", user.username)
        user.save()
        return Response(
            {"message": "User details updated successfully"}, status=status.HTTP_200_OK
        )

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response(
            {"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = AllowAny
    serializer_class = RegisterSerializer


class LoginAPI(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
