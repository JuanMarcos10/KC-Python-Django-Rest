from django.contrib import admin
from django.utils.safestring import mark_safe

from blogs.models import Blog

admin.site.site_title = 'Wordplease Admin System'
admin.site.site_header = 'Wordplease Admin System'
admin.site.index_title = 'Wordplease Admin System'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_select_related = ['owner']
    list_display = ('title', 'get_img', 'id', 'text', 'owner', 'creation_date', 'get_owner_name')
    list_filter = ('owner', 'category',)
    search_fields = ['title', 'description', 'owner__first_name', 'owner__last_name']
    readonly_fields = ['get_img', 'get_owner_name', 'creation_date', 'modification_date']
    fieldsets = [
        [None, {
            'fields': ['title', 'text', 'get_img', 'url']
        }],
        ['Properties', {
            'fields': ['owner', 'category']
        }],
        ['Description', {
            'fields': ['description']
        }],
        ['Dates', {
            'fields': ['creation_date', 'modification_date'],
            'classes': ['collapse']
        }]
    ]

    def get_owner_name(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    get_owner_name.short_description = 'Owner'
    get_owner_name.admin_order_field = 'owner__first_name'

    def get_img(self, obj):
        return mark_safe('<img src="{0}" height="50">'.format(obj.url))

    get_img.short_description = 'Image'
    get_img.admin_order_field = 'name'

