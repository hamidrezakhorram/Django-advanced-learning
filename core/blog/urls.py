from django.urls import path
from .views import IndexView
urlpatterns =[
    path('cbv', IndexView.as_view() , name='cbc' ),
]