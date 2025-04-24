
from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
# for sending email

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializers

from django.contrib.auth import update_session_auth_hash

from rest_framework import generics
from rest_framework import status



class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"https://glamify-backend-tp2c.onrender.com/account/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)



def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class UserLoginApiView(APIView):
    def post(self, request):
        user_login_serializer = serializers.UserLoginSerializer(data=request.data)
        
        if user_login_serializer.is_valid():
            username = user_login_serializer.validated_data['username']
            password = user_login_serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Invalid Credential"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(user_login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogoutApiView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')
    


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers



class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user and user.is_staff:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials or not an admin.'}, status=status.HTTP_400_BAD_REQUEST)



class AdminLogoutView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization').split()[1]  
        
        try:
            Token.objects.get(key=token).delete()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeAPIView(APIView):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        
        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect."})
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return Response({"message": "Password changed successfully."})


