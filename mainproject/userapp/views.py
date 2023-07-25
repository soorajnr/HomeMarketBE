from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import User
from .serializer import UserSerializer
from rest_framework import generics 
from django.http import request
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from userapp.models import User


class UserDataViewSet(viewsets.ViewSet):

    def create(self, request):
            mobile = request.data.get('mobile')
            print("valid")  
            print(mobile)
             #rite function to send otp   
            try:
                user = User.objects.get(mobile=mobile)  # Get the user with the given mobile value
                print('User found! Name:', user.name)
                userdata={
                     'name':user.name,
                     'mobile':user.mobile
                     }
                return Response({'message': 'Data saved successfully','user':userdata}, status=201)

            except User.DoesNotExist:    
                userdata=User.objects.create(mobile=mobile,name="siva")
                userdata.save()
                    # Return a success response
                return Response({'message': 'Data saved successfully'}, status=201)
            
          

class UserDetail(generics.RetrieveDestroyAPIView):
    queryset=User.objects.all()
    # if request.method=='POST':
    #     user_data=JSONParser().parse(request)
    #     user_serializer=UserSerializer(data=user_data)
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    serializer_class=UserSerializer

#get user 

class UserList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer   

    