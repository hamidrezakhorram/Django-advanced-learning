from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.detail import DetailView
from .forms import ContactForm
from .models import Post
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "hamid"
        context["post"] = Post.objects.all()
        return context


class RedirectWeb(RedirectView):
    pattern_name = "blog:cbv"


class BlogPost(LoginRequiredMixin, ListView):
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        posts = Post.objects.all()
        return posts


class PostDetailView(DetailView):
    model = Post


class ContactPost(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = None

    def get_success_url(self):
        return redirect("blog:post")


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "status", "category", "content", "published_date"]
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "status", "category", "content", "published_date"]
    success_url = "/blog/post/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"
