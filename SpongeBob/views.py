from django.shortcuts import render
from rest_framework import generics
from .models import SpongeBob
from .serializers import PostSerializer

# Create your views here.

class PostsList(generics.ListCreateAPIView):
    queryset = SpongeBob.objects.all()
    serializer_class = PostSerializer

class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpongeBob.objects.all()
    serializer_class = PostSerializer
