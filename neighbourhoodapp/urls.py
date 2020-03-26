from django.contrib import admin
from django.urls import path,re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='index'),
    path('c/', views.posted, name='sigxnup'),
    path('signup/', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('profile/', views.myprofile, name='profile'),
re_path(r'^update/profile', views.updatemyprofile, name='update_profile'),
re_path(r'^api-token-auth/', obtain_auth_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^update/(\d+)', views.comment, name='comment'),
    re_path(r'^updates/(\d+)', views.updates, name='updates'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
