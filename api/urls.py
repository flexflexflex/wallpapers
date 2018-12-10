from django.urls import path, include
from apps.pictures.views import PicturesViewSet

app_name = 'api'

pictures_urls = [
    path('', PicturesViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', PicturesViewSet.as_view({'get': 'retrieve'}))
]

urlpatterns = [
    path('pictures/', include(pictures_urls)),
]
