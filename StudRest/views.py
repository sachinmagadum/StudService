from rest_framework import generics

from .models import StudentModel
from .serializers import PostSerializer




class PostList(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = PostSerializer