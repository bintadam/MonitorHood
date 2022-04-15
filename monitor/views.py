from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
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
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def login_view(request):
    context = {}
    return render (request, 'acounts/login.html', context)


def logout_view(request):    
    return redirect ('accounts:login')
