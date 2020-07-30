from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

# Create your views here.

def post_list(request):
    print("tws23")
    posts = Post.objects.all().order_by("date") # grabs all posts from db ordered by date
    return render(request, "posts/post_list.html", {"posts": posts}) # create dic to send to template with data retrieved from db

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post' : post }) # retrieves content for each post