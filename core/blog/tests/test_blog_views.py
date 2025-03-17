from django.test import TestCase , Client
from django.urls import reverse
class ViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()


    def test_blog_index_url_successful(self):
        url = reverse('blog:cbv')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
