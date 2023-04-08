from django.contrib import admin

# Register your models here.
from.models import Topic, Entry

class PostAdmin(admin.ModelAdmin):
    list_display=('text', 'slug', 'owner', 'date_added', 'status')
    list_filter=('status', 'created', 'date_added', 'owner')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('text',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'date_added'
    ordering = ['status', 'date_added']

admin.site.register(Topic, PostAdmin)
admin.site.register(Entry)
