from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import Blogs


def blog(request):
    """ A view to display all blogs """
    # Get all the blog posts in the database and order
    # by date
    blogs = Blogs.objects.all().order_by('-date')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/all_blogs.html', context)
