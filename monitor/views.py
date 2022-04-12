from django.shortcuts import redirect, render

# Create your views here.
def register(request):
    context = {}
    return render (request, 'acounts/register.html', context)


def login_view(request):
    context = {}
    return render (request, 'acounts/login.html', context)


def logout_view(request):    
    return redirect ('accounts:login')
