from django.test import SimpleTestCase
from django.urls import reverse , resolve
from ..views import IndexView , PostDetailView

class TestUrl(SimpleTestCase):

    def test_blog_index_url_resolve(self):
        url = reverse('blog:cbv')
        self.assertEqual(resolve(url).func.view_class , IndexView)

    def test_blog_detain_url_resolve(self):
        url = reverse('blog:post-detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class ,  PostDetailView)


