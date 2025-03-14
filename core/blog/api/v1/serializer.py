from rest_framework import serializers
from blog.models import Post , Category
from accounts.models import Profile
# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length =255)
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class PostSerializers(serializers.ModelSerializer):
    created_date = serializers.ReadOnlyField
    snippet = serializers.ReadOnlyField(source ='get_snippet')
   #category =serializers.SlugRelatedField(many = False , slug_field = 'name' , queryset = Category.objects.all())
    
    class Meta:
        model =Post
        fields=['title' ,'auther','status','created_date','published_date','content','snippet','category']
        read_only_fields = ['status','auther']

    def to_representation(self, instance):
        request =self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet' , None)
        else :
            rep.pop('content' , None)    
        rep['category']=CategorySerializers(instance.category).data
        return rep
    
    # def create(self, validated_data):
    #     validated_data['auther']=Profile.objects.get(user__id = self.context.get('request').user.id)
    #     return super().create(validated_data)