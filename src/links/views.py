from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView

from links.serializers import LinkSerializer
from .models import Link

# Create your views here.
class PostListApi(ListView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(UpdateView):
    queryset = Link.objects.filter(active=True)
    serializer = LinkSerializer
    
class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer = LinkSerializer
    
