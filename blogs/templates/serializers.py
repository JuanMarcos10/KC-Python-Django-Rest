from rest_framework.serializers import ModelSerializer

from blogs.models import Blog


class PhotoListSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'name', 'url']


class PhotoSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'name', 'url', 'description', 'creation_date', 'modification_date',
                  'license', 'visibility', 'owner']
        read_only_fields = ['id', 'creation_date', 'modification_date']