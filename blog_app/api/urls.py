from django.urls import path
from .views import api_post_detail_view, api_post_udpate_view

urlpatterns = [
    path('detail/<slug>', api_post_detail_view),
    path('update/<slug>', api_post_udpate_view),
]