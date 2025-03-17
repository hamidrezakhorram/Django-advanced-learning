from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path("cbv", IndexView.as_view(), name="cbv"),
    path("go-to-cbv/", RedirectWeb.as_view(), name="go-to-cbv"),
    path("post/", BlogPost.as_view(), name="post"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/contact", ContactPost.as_view(), name="post-contact"),
    path("post/create", PostCreateView.as_view(), name="create-post"),
    path(
        "post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"
    ),
    path(
        "post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
