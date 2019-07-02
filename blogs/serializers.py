from rest_framework.serializers import ModelSerializer

from blogs.models import Blog


class BlogListSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'owner', 'title', 'url']


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'owner', 'title', 'url', 'description', 'creation_date', 'modification_date',
                  'category', 'visibility']
        read_only_fields = ['id', 'creation_date', 'modification_date', 'owner']
