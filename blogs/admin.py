from django.contrib import admin

from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'text', 'owner', 'creation_date')
    list_filter = ('owner', 'category',)
    search_fields = ['title', 'description']


admin.site.register(Blog, BlogAdmin)
