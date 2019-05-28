from django.forms import ModelForm

from blogs.models import Blog


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'text', 'description', 'url', 'category']
