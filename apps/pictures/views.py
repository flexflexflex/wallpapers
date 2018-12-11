from rest_framework import viewsets
from rest_framework import generics

from apps.pictures.serializers import PictureSerializer, TagSerializer
from .models import Picture, Tag


class PicturesViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.filter(is_visible=True).prefetch_related('tags')
    serializer_class = PictureSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(category=self.kwargs.get('category'))

        tags = self.request.query_params.get('tags')
        if tags:
            tags = tags.split(',')
            for tag in tags:
                queryset = queryset.filter(tags__name=tag)

        return queryset


class TagsListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return super().get_queryset().filter(category=self.kwargs.get('category'))
