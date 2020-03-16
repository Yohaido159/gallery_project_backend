import os
import io
import requests
import zipfile

from django.http import StreamingHttpResponse, HttpResponse, JsonResponse

from .models import Gallery, Image

from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, ParseError
from rest_framework.decorators import action, parser_classes
from rest_framework.response import Response
from .serializers import SerializerGallery, SerializerGalleryImages
from .permissions import ListGalleryPermissions, DetailGalleryPermissions

from celery import shared_task


# route
class ListGalleryImages(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = SerializerGalleryImages
    # permission_classes = (DetailGalleryPermissions,)

    def list(self, request):
        queryset = Gallery.objects.all()
        serializer = SerializerGalleryImages(queryset, many=True)
        return Response(serializer.data)


# list-gallery
class ListGallery(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = SerializerGallery
    # permission_classes = (ListGalleryPermissions,)


# list-gallery/<int:pk>
class DetailGallery(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = SerializerGallery
    permission_classes = (DetailGalleryPermissions,)


# list-gallery-images/<int:pk>
class DetailGalleryImages(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = SerializerGalleryImages
    permission_classes = (DetailGalleryPermissions,)


# download
def download(request):
    url = request.GET.get("url")
    filename = os.path.basename(url)
    r = requests.get(url, stream=True)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Disposition'] = f'attachement; filename="{filename}"'
    return response


def download_multiple(request):

    filenames = []
    buffer = io.BytesIO()

    # יוצא את הזיפ
    zip_file = zipfile.ZipFile(buffer, 'w')

    # מקבל רשימה של יו אר אל
    url = request.GET.get("url")

    # מוציא את השם משתמש מתוך הסטרינג
    gal_name = url.split("/")[6:7]
    gal_name = "".join(gal_name)

    # כותב כל תמונה במקום שלה בזיפ
    url_list = request.GET.getlist('url')
    for value in url_list:
        res = requests.get(value)
        name = os.path.split(value)[1]
        zip_file.writestr(name, res.content)
    zip_file.close()

    response = HttpResponse(buffer.getvalue())
    response['Content-Type'] = 'application/x-zip-compressed'
    response['Content-Disposition'] = f'attachment; filename={gal_name}.zip'

    return response
