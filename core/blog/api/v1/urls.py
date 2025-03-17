from django.urls import path, include
from . import view
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("post", view.PostViewset, basename="post")

urlpatterns = [
    # path('post/' , view.PostList.as_view() , name='post-list'),
    # path('post/<int:pk>/' , view.PostDetailView.as_view() , name='post-detail'),
    # path('post/', view.PostViewset.as_view({'get':'list' , 'post':'create'}), name = 'post-list'),
    # path('post/<int:pk>/' , view.PostViewset.as_view({'get':'retrieve' , 'put':'update' ,'patch' :'partial_update' ,'delete':'destroy'}), name = 'post-detail'),
    path("", include(router.urls))
]
