from rest_framework.viewsets import ModelViewSet

from apps.pictures.serializers import PictureSerializer
from .models import Picture


class PicturesViewSet(ModelViewSet):
    queryset = Picture.objects.filter(is_visible=True).prefetch_related('tags')
    serializer_class = PictureSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        tags = self.request.query_params.get('tags')
        if tags:
            tags = tags.split(',')
            for tag in tags:
                queryset = queryset.filter(tags__name=tag)

        return queryset


