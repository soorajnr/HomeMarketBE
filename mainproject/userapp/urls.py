from django.urls import path,include
from django import urls
from .views import UserDetail,UserList,UserDataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('userdata', UserDataViewSet, basename='user-data')

urlpatterns=[

    path('users/',UserList.as_view(),name='Users'),
    path('user/<int:pk>',UserDetail.as_view(),name="User"),
    path('', include(router.urls)),

    # path('userdata/',UserDataViewSet.as_view(),name="userdata")s
]
