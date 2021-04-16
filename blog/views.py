from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
# Create your views here.


# def home(request):
#     context = {
#         'title': 'Ny posts',
#         'posts': Post.objects.all(),
#     }
#     return render(request, 'home.html', context=context)


class PostListViews(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    # if you want the newest post put [-dete_posted]
    ordering = ['-dete_posted']
    paginate_by = 5


class UserPostListViews(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    # if you want the newest post put [-dete_posted]
    paginate_by = 5

    def get_queryset(self):
        # kwargs: is query pramter
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(auther=user).order_by('-dete_posted')


class DetailListViews(DetailView):
    model = Post
    template_name = 'post_details.html'


class CreatePostViews(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)


class UpdatePostViews(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class DeletePostViews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


def about(request):
    return render(request, 'about.html', context={'title': 'About'})
