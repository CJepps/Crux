from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(
        max_length=60, blank=False, null=False, unique=True)
    image = models.ImageField(null=True, blank=True)
    image_caption = models.CharField(max_length=60, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    subheading1 = models.CharField(max_length=60, blank=True, null=True)
    para1 = models.TextField(blank=False, null=False)
    subheading2 = models.CharField(max_length=60, blank=True, null=True)
    para2 = models.TextField(blank=True, null=True)
    subheading3 = models.CharField(max_length=60, blank=True, null=True)
    para3 = models.TextField(blank=True, null=True)
    subheading4 = models.CharField(max_length=60, blank=True, null=True)
    para4 = models.TextField(blank=False, null=False)
    subheading5 = models.CharField(max_length=60, blank=True, null=True)
    para5 = models.TextField(blank=True, null=True)
    subheading6 = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.title
