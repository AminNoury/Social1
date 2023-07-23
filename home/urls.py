from django.urls import path
from . import views
from posts.views import PostDetailView


app_name = 'home'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),




]