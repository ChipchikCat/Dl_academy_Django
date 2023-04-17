from django.contrib import admin
from.models import Image
from django.utils.safestring import mark_safe

class ImageAdmin(admin.ModelAdmin):

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')

admin.site.unregister(Image)  
admin.site.register(Image,ImageAdmin)
