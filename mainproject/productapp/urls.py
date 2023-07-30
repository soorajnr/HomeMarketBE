from django.urls import path,include
from .views import ProductDetail ,CategoeryDetail,ProductUpdateViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('productUpdate', ProductUpdateViewset, basename='user-dataproductUpdate')
urlpatterns=[
    path('allcategory/',CategoeryDetail.as_view(),name="allcategory"),
    path('allproduct/',ProductDetail.as_view(),name="allproduct"),
    # path('productUpdate/',ProductUpdateViewset.as_view(),name="productUpdate")
    path('', include(router.urls)),

]