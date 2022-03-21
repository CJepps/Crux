from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import Blogs


def blog(request):
    """ A view to display all blogs """
    blogs = Blogs.objects.all().order_by('-date')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/all_blogs.html', context)


def blog_detail(request, blogss_id):
    """ A view to display individual blogs """
    blog = get_object_or_404(Blogs, pk=blogss_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blogs/blog_details.html', context)
