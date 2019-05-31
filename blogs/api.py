from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogs.models import Blog
from blogs.permissions import BlogPermission
from blogs.serializers import BlogListSerializer, BlogSerializer
from blogs.views import BlogList


class BlogsAPI(BlogList, ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return BlogListSerializer if self.request.method == 'GET' else BlogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogDetailAPI(BlogList, RetrieveUpdateDestroyAPIView):

    permission_classes = [BlogPermission]

    serializer_class = BlogSerializer

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)