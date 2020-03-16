from django.contrib import admin
from .models import Gallery, Image, ImageS3

from django.contrib import admin


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["unique_id"]


admin.site.register(Gallery)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageS3, ImageAdmin)
