from django.contrib import admin
from .models import Blogs


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'date',
        'para1',
        'para2',
        'para3',
    )


admin.site.register(Blogs, BlogAdmin)
