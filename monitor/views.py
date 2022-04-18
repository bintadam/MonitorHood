from django.shortcuts import render, redirect
from django.http import response
from django.contrib.auth.decorators import login_required
from django.http.response import Http404, HttpResponseRedirect
from .models import Neighbour, Profile ,Business, Post
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from .forms import *

@login_required(login_url='accounts/login/')
def home(request):
    try:
        area = Neighbour.objects.all()
    except Exception as e:
        raise Http404
    return render(request, "home.html", {"area": area})


@login_required(login_url='accounts/login/')
def createNeighbourHood(request):
    if request.method == "POST":
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            Area = form.save(commit = False)
            Area.save()
        return redirect("home")
    else:
        form = NeighbourHoodForm()
    return render(request, "CreateNeighbourhood.html", {"form": form})


@login_required(login_url='accounts/login/')
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileForm()
    return render(request, "profile.html", {"form": form, "profile": profile})


@login_required(login_url='accounts/login/')
def post(request):
    posts = Post.objects.all().order_by('-posted_on')
    return render(request, "post.html", {"posts": posts})		


@login_required(login_url='accounts/login/')
def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.neighbourhood = request.user.profile.neighbourhood
            post.posted_by = request.user
            post.save()
            return redirect("post")
    else:
        form = PostForm()
    return render(request, "newPost.html", {"form": form})


@login_required(login_url='accounts/login/')
def business(request):
    user = User.objects.filter(id = request.user.id).first()
    profile = Profile.objects.filter(user = user).first()
    if request.method == "POST":
        business_form = BusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = Business(name = request.POST['name'], neighbourhood = profile.neighbourhood)
            business.save()
        return redirect('business')
    else:
        business_form = BusinessForm()
    return render(request, "business.html", {"business": business_form})
