from django.urls import path , include
from . import view
from django.views.generic.base import RedirectView

app_name ='api-v1'

urlpatterns =[
   
    path('post/' , view.PostList.as_view() , name='post-list'),
    path('post/<int:pk>/' , view.PostDetailView.as_view() , name='post-detail'),  

]
