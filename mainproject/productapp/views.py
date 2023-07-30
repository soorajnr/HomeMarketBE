from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Product,Category_class
from .serializer import ProductSerializer,CategorySerializer
from rest_framework.response import Response
from userapp.models import User
# Create your views here.

class ProductDetail(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class CategoeryDetail(generics.ListCreateAPIView):
    queryset=Category_class.objects.all()
    serializer_class=CategorySerializer   

class ProductUpdateViewset(viewsets.ViewSet):
    def create(self,request):
        
        name=request.data.get('name')
        print(name)
        price=request.data.get('price')
        description=request.data.get('description')
        category_id=request.data.get('category')
        location=request.data.get('location')
        # photo=request.data.get('photo')
        # quantity=request.data.get('quantity')
        # price_cat=request.data.get('price_cat')
        seller_id=request.data.get('seller')
        print(seller_id)

        try:
            category=Category_class.objects.get(id=category_id)

            print("okay")
            seller=User.objects.get(id=seller_id)
            print("y")
            product_data=Product.objects.create(
            name=name,
            price=price,
            description=description,
            category=category,
            location=location,
            # photo=photo,
            # quantity=quantity,
            # price_cat=price_cat,
            seller=seller, )
            product_data.save()
            print("sets")
            return Response({'message': 'Data saved successfully'}, status=201)
        except:
            return Response({'message': 'Data saving failed'}, status=201)
                
