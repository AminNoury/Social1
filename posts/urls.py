from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail')

]
