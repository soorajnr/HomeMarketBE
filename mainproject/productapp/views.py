from django.shortcuts import render
from rest_framework import generics

from .models import Product,Category_class
from .serializer import ProductSerializer,CategorySerializer
# Create your views here.

class ProductDetail(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class CategoeryDetail(generics.ListCreateAPIView):
    queryset=Category_class.objects.all()
    serializer_class=CategorySerializer   

