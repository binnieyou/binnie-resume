from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog.html', {'posts': posts})