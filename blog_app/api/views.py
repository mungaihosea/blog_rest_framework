from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PostSerializer
from blog_app.models import Post


@api_view(['GET'])
def api_blog_detail_view(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PostSerializer(blog_post)
        return Response(serializer.data)