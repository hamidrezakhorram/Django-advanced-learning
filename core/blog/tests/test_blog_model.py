from django.test import TestCase
from blog.models import Post
from accounts.models import User , Profile
from datetime import datetime
class ModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email = "test@test.com",password = "@test12345678")
        
        self.profile =Profile.objects.create(
            user =self.user,
            first_name = 'test_first_name',
            last_name = 'test_last_name',
            description = 'test description'
        )

       
     
    def test_create_post_valid_data(self):
        
        post = Post.objects.create(
            auther =self.profile,
            title ='test',
            content = 'description',
            category =None,
            published_date =datetime.now()


        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())