from rest_framework import serializers
from blog.models import Post
# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length =255)

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model =Post
        fields=['title' ,'auther','status','created_date','published_date','content']