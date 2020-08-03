from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from . import forms

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by("-date") # grabs all posts from db ordered by date
    return render(request, "posts/post_list.html", {"posts": posts}) # create dic to send to template with data retrieved from db

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post' : post }) # retrieves content for each post

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == "POST": # when the submit btn is pressed
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user # set the current logged in user as the post writer
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, "posts/post_create.html", { 'form' : form })

@login_required(login_url="/accounts/login")
def post_own(request):
    posts = Post.objects.filter(author=request.user) # filter posts by current logged in user
    return render(request, "posts/post_own.html", {"posts": posts})