from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from blogs.models import Blog
from blogs.serializers import BlogListSerializer, BlogSerializer


class BlogsAPI(ListCreateAPIView):

    queryset = Blog.objects.all()

    def get_serializer_class(self):
        return BlogListSerializer if self.request.method == 'GET' else BlogSerializer


class BlogDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
