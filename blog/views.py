from django.shortcuts import render
from . models import Blog

def allblogs(request):
	blogs = Blog.objects
	return render(request, 'allblogs.html',{'blogs':blogs})
	


def index(request):
	post_list = Post.objects.all()
	return render(request,'index.html',{'post_list':post_list,})

# Create your views here.
