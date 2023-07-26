from rest_framework import serializers
from .models import Product,Category_class


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category_class
        fields='__all__' 