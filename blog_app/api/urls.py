from django.urls import path
from .views import api_blog_detail_view

urlpatterns = [
    path('detail/<slug>', api_blog_detail_view)
]