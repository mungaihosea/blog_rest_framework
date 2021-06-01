from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from blog_app.models import Post

from blog_app.api import serializers

@api_view(['GET'])
def api_post_detail_view(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_DOES_NOT_EXIST)
    
    if request.method == 'GET': #this is only necessary if the endpoint handles more than request type ie GET, POST
        serializer = PostSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
def api_post_udpate_view(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_DOES_NOT_EXIST)
    
    if request.method == 'PUT': #put is used to like modify a particular record in the database
        serializer = PostSerializer(blog_post, data= request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = 'update_successfull'
            return Response(data = data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def api_post_delete_view(request, slug):
    try:
        blog_post = Post.objects.get(id = slug)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_DOES_NOT_EXIST)
    
    if request.method == 'DELETE': #put is used to like modify a particular record in the database
        data = {}
        operation = blog_post.delete()
        if operation:
            data['success'] = "deleted successfully"
            return Response(data = data)
        else:
            data['failure'] = 'delete failed'
            return Response(data = data)
