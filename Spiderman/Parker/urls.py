from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list, name="product_list"),
    path('review/', review_list, name="review_list"),
]
