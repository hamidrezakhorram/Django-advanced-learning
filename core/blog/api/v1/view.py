from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializers
from blog.models import Post
from rest_framework  import status
from django.shortcuts import get_object_or_404
@api_view(['GET' , 'POST'])
def postList(request):
    if request.method == 'GET':
       posts = Post.objects.filter(status=True)
       serializer =PostSerializers(posts , many =True)
       return Response(serializer.data) 
    elif request.method =='POST':
        serializer = PostSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
       
            
        
@api_view(['GET' , 'PUT','DELETE'])
def postDetail(request , id):
    post = get_object_or_404(Post , pk=id)
    if request.method =='GET':
        serializer =PostSerializers(post)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = PostSerializers(post , data =request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
    elif request.method =='DELETE':
        post.delete()
        return Response('item removed successfully' , status=status.HTTP_204_NO_CONTENT)
    
     
   