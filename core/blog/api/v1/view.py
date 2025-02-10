from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializers
from blog.models import Post
from rest_framework  import status
from django.shortcuts import get_object_or_404
@api_view()
def postList(request):
    posts = Post.objects.filter(status=True)
    serializer =PostSerializers(posts , many =True)
    return Response(serializer.data)

@api_view()
def postDetail(request , id):
    post = get_object_or_404(Post , pk=id)
    serializer =PostSerializers(post)
    return Response(serializer.data)
    
    # try:
    #      post = Post.objects.get(pk=id)
    #      serializer =PostSerializers(post)
    #      return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response("post does not excite",status=status.HTTP_404_NOT_FOUND)    
   