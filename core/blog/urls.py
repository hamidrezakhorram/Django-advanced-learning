from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

app_name ='blog'

urlpatterns =[
    path('cbv', IndexView.as_view() , name='cbv' ),
    path('go-to-cbv/', RedirectWeb.as_view(), name='go-to-cbv'),
    path('post/',BlogPost.as_view(),name='post'),
    path('post/<int:pk>' ,PostDetailView.as_view() , name='post-detail' )
    
]