from django.shortcuts import render
from django.views.generic import TemplateView ,RedirectView ,ListView
from django.views.generic.detail import DetailView

from .models import Post
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='hamid'
        context['post']=Post.objects.all()
        return context
    
    
class RedirectWeb(RedirectView):
    pattern_name = "blog:cbv"    
    
 
class BlogPost(ListView):
    context_object_name ='posts'    
    paginate_by = 2
    def get_queryset(self):
        posts = Post.objects.all()
        return posts
    
    
class PostDetailView(DetailView):
    model = Post    