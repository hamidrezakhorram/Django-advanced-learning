from rest_framework.response import Response
from .serializer import PostSerializers
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import StandardResultsSetPagination


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)


# viewSet in CBV


class PostViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializers
    pagination_class = StandardResultsSetPagination
    queryset = Post.objects.filter(status=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "auther"]
    search_fields = ["title", "auther__first_name"]
    ordering_fields = ["published_date"]

    # @action(detail=False)
    # def test_extra():
    #      return Response({'ok': 'blabla'})
