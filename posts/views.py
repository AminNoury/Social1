from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from .forms import PostCreateUpdateForm
from .models import Post

class PostDetailView(View):

    def get(self, request, post_id, post_slug):
        post = Post.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'posts/detail.html', {'post': post})

class PostDeleteView(LoginRequiredMixin, View):

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if request.user.id == post.user.id:
            post.delete()
            messages.success(request, 'your post deleted', 'success')
        else:
            messages.error(request, 'you cant delete this post', 'danger')
        return redirect('home:home')

class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(pk=kwargs['post_id'])
        super().setup(request, *args, **kwargs)


    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request, 'you cant update this post', 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'posts/update.html', {'form': form})


    def post(self, request, *args, **kwargs):
         post = self.post_instance
         form = self.form_class(request.POST, instance=post)
         if form.is_valid():
             new_post = form.save(commit=False)
             new_post.slug = slugify(form.cleaned_data['body'][:30])
             new_post.save()
             messages.success(request, 'your post updated', 'success')
             return redirect('posts:post_detail', post.id, post.slug)

class PostCreateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'posts/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'you create the post', 'success')
            return redirect('posts:post_detail', new_post.id, new_post.slug)
