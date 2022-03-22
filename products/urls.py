from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('addcomment/<int:id>', views.add_comment, name='addcomment'),
    path('add/<int:id>', views.add_product, name='addproduct'),
]
