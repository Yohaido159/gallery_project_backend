from django.urls import path, re_path
from .views import ListGallery, ListGalleryImages
from .views import DetailGallery, DetailGalleryImages
from .views import download, download_multiple

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("route", ListGalleryImages, basename="list-gallery-images")
router.register("list-gallery", ListGallery, basename="list-gallery")

urlpatterns = [
    path("list-gallery/<int:pk>", DetailGallery.as_view(), name="detail-api"),
    path("list-gallery-images/<int:pk>",
         DetailGalleryImages.as_view(), name="images-detail-api"),
    path("download/", download, name="download"),
    path("download-multiple/", download_multiple, name="download_multiple"),
]

urlpatterns += router.urls
