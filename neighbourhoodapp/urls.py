from django.contrib import admin
from django.urls import path,re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

<<<<<<< HEAD
urlpatterns = [
    path('', views.home, name='home'),
    path('auth/signup/', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('profile/', views.myprofile, name='profile'),
re_path(r'^update/profile', views.updatemyprofile, name='update_profile'),
re_path(r'^api-token-auth/', obtain_auth_token)

]
=======
urlpatterns=[
    
]
>>>>>>> f43f7746606b0f90794783a828411cdf49829290