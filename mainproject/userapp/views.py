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
import random
import requests
 


class UserDataViewSet(viewsets.ViewSet):

    def create(self, request):
            global mobile
            mobile = request.data.get('mobile')
            print("valid")  
            print(mobile)
             #rite  function to send otp 
            global random_number
            random_number = random.randint(10000, 99999)
            print(random_number)
            # try: 
            #     url = "https://2factor.in/API/V1/603257ec-b14c-11ed-813b-0200cd936042/SMS/{mobile}/{random_number}/OTP1"
            #     params = {'mobile': mobile,
            #             'random_number': random_number}
            #     url = url.format_map(params)
            #     payload = {}
            #     headers = {}

            #     response = requests.request("GET", url, headers=headers, data=payload)

            #     print(response.text)
            #     pass
            # except:
            #      pass    
 
            try:
                global user
                user = User.objects.get(mobile=mobile)  # Get the user with the given mobile value
                print('User found! Name:', user.name)
                userdata={
                     'name':user.name,
                     'mobile':user.mobile
                     }
                return Response({'message': 'Data saved successfully','user':userdata,'success':True}, status=201)
            # return Response({'message': 'otp send succsfully'}, status=201)

            except User.DoesNotExist:    
                # userdata=User.objects.create(mobile=mobile,name="siva")
                # userdata.save()
                    # Return a success response
                return Response({'message': 'user not found','success':False },status=201)
            
class Verify_otp(viewsets.ViewSet):           
    def create(self,request):
     
        
          Entered_otp=request.data.get('entered_otp')
          Entered_otp=int(str(Entered_otp))
          print(type(Entered_otp))
          print("otpenterd:", Entered_otp)
          global random_number
          print(type(random_number))

          if random_number==Entered_otp:
            # try:
            #         global user
            #         global mobile
            #         print(mobile)
            #         user = User.objects.get(mobile=mobile)  # Get the user with the given mobile value
            #         print('User found! Name:', user.name)
            #         userdata={
            #             'name':user.name,
            #             'mobile':user.mobile
            #             }
                    # return Response({'message': 'otp verified user alread exists ','user':userdata,'success':True}, status=201)

            # except User.DoesNotExist:    
            #     # userdata=User.objects.create(mobile=mobile,name="siva")
            #     # userdata.save()
            #         # Return a success response
            #     # return Response({'message': 'Data saved successfully','success':False },status=201)
                return Response({'message':'OTP verification succsed ','success':True},status=201)
          else:
                return Response({'message':'OTP verification failed','success':False},status=201)
    #  print("kop")     
    #  return Response({'message':'OTP verification failed','success':False},status=201)

          


class UserDetail(generics.RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

#get user 

class UserList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer   

    