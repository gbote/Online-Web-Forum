from hashlib import new
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *

def index(request):
    return render(request, "pages/index.html", {'posts':all_posts})

def post_detail(request, post_id):
    post = find_post_by_id(post_id)
    if request.method == 'POST':
        input_data = {
            'body': request.POST['body'],
            'author': request.POST['author'],
            'post_id': post_id
        }
        new_comment = Comment(**input_data)
        post.add_comment(new_comment)
    return render(request, "pages/post_detail.html", {'post':post})

def new_post(request):
    if request.method == 'POST':
        input_data = {
            'title': request.POST['title'],
            'body': request.POST['body'],
            'author': request.POST['author']
        }
        new_post = Post(**input_data)
        Post.add_post(new_post)
        return redirect(reverse("post_detail", args=[new_post.id]))
    return render(request, "pages/new_post.html")