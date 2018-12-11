from .models import Picture, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', ]


class PictureSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        exclude = ['category', 'is_visible']

    @staticmethod
    def get_tags(picture):
        return picture.tags.all().values_list('name', flat=True)

