from django.shortcuts import render
from .models import Post # the dot means current directory or current
	# application. so techinically this means from the same directory
	# that has views.py, import models (no need to .py to models)
from django.utils import timezone

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

