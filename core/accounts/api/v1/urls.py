from django.urls import path , include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

name = 'api-v1'
urlpatterns=[
   path('registration/', views.RegistrationView.as_view() , name = 'registration-api' ),
   path('token/login/', views.CustomAuthToken.as_view(), name= 'token-login'),
   path('token/logout/', views.CustomDiscardToken.as_view(), name ='token-logout'),
   path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
   path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
   path('jwt/verify/',TokenVerifyView.as_view(), name= 'jwt-verify'),
]

