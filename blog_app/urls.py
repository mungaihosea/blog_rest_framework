from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="list_view"),
    path('detail/<slug:id>/', detail_view, name="detail_view"),
]