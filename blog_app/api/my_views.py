from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from blog_app.models import Post
from django.contrib.auth.models import User

@api_view(['GET'])
def api_detail_view(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)

    except Post.DoesNotExist:
        data = {}
        data['error'] = "an error occured"
    return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def api_delete_view(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)
    except Post.DoesNotExist:
        data = {'error':"an error occured"}
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        data = {}
        operation = blog_post.delete()
        if operation: 
            data['success'] = 'item deleted successfully'
            return Response(data=data)
        else:
            data['failed'] = 'delete failed'
            return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_edit_request(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)
    except Post.DoesNotExist:
        data = {'error':"an error occured"}
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = {}
        serializer = PostSerializer(blog_post, request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'blog post modified successfully'
            return Response(data = data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['POST'])
def api_post_view(request):
    user = User.objects.all()[0]
    blog_post = Post(user = user)

    serializer = PostSerializer(blog_post, request.data)
    data = {}
    if serializer.is_valid():
        data['success'] = 'Blog post created successfully'
        return Response(data = data)
    else:
        return Response(data = serializer.errors)