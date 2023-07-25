# from django.urls import path
# from . import views
#
# app_name = 'posts'
# urlpatterns = [
#     # path('posts/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
#     # path('posts/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
#     # path('posts/update/<int:post_id>', views.PostUpdateView.as_view(), name='post_update'),
#
# ]

from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/update/<int:post_id>', views.PostUpdateView.as_view(), name='post_update')


]