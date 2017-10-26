from django.contrib import admin
from web.models import Image
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
