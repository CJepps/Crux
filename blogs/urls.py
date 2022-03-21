from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blogs'),
    path('<int:blogss_id>/', views.blog_detail, name='blog_detail')
]
