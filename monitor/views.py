from django.shortcuts import render

# Create your views here.
def register(request):
  context = {}
  return render (request, 'acounts/register.html', context)