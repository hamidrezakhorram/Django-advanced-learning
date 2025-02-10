from django.urls import path , include
from . import view
from django.views.generic.base import RedirectView

app_name ='api-v1'

urlpatterns =[
   
    path('post/' , view.postList , name='post-list'),
    path('post/<int:id>/' , view.postDetail , name='post-detail'),  

]
