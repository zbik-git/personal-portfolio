from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_all(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_all.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
