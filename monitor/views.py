from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def homepage(request):
	return render(request=request, template_name='registration/home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})


def createNeighbourHood(request):
    if request.method == "POST":
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            mtaa = form.save(commit = False)
            mtaa.save()
        return redirect("home")
    else:
        form = NeighbourHoodForm()
    return render(request, "create_neighbourhood.html", {"form": form})


def post(request):
    posts = Post.objects.all().order_by('-posted_on')
    return render(request, "post.html", {"posts": posts}

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("registration:homepage")
