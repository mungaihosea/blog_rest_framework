from django.urls import path
from .views import api_detail_view, api_post_view, api_delete_view, api_update_view

urlpatterns = [
    path('detail/<slug>', api_detail_view),
    path('update/<slug>', api_update_view),
    path('post', api_post_view),
    path('delete/<slug>', api_delete_view),
]