from django.urls import path
from .views import ProductDetail ,CategoeryDetail

urlpatterns=[
    path('allcategory/',CategoeryDetail.as_view(),name="allcategory"),
    path('allproduct/',ProductDetail.as_view(),name="allproduct")
]