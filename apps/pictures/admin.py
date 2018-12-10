from django.contrib import admin

from .models import Category, Tag, Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'description']
    list_filter = ['category', 'tags']
    filter_vertical = ['tags']
    readonly_fields = ('image_tag',)


admin.site.register(Category)
admin.site.register(Tag)
