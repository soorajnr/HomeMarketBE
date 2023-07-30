from django.urls import path,include
from django import urls
from .views import UserDetail,UserList,UserDataViewSet,Verify_otp
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('userdata', UserDataViewSet, basename='user-data'),
router.register('verifyotp', Verify_otp, basename='verify-otp')

urlpatterns=[

    path('users/',UserList.as_view(),name='Users'),
    path('user/<int:pk>',UserDetail.as_view(),name="User"),
    # path('verifyotp/',Verify_otp.as_view(),name="verify-otp"),
    path('', include(router.urls)),

    # path('userdata/',UserDataViewSet.as_view(),name="userdata")s
]
