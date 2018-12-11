from django.urls import path, include
from apps.pictures.views import PicturesViewSet, TagsListView

app_name = 'api'

pictures_urls = [
    path('<str:category>/', PicturesViewSet.as_view({'get': 'list'})),
    path('<str:category>/tags/', TagsListView.as_view()),
    path('<int:pk>/', PicturesViewSet.as_view({'get': 'retrieve'}))
]

urlpatterns = [
    path('pictures/', include(pictures_urls)),
]
