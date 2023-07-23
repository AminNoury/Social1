from django.shortcuts import render
from django.views import View

from .models import Post

class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(id=post_id, slug=post_slug)
        return render(request, 'posts/detail.html', {'post': post})


