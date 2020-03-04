from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the post index.")


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
