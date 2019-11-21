from django.shortcuts import render
from .models import Friend 
def home(request):
	friends = Friend.objects
	return render(request,'home.html' , {'friends' :friends})
# Create your views here.
