import os
import io
import string
import requests
import zipfile
import boto3
from storages.backends.s3boto3 import S3Boto3Storage

from django.http import StreamingHttpResponse, JsonResponse
from django.utils.crypto import get_random_string
from django.core.files.base import ContentFile
from django.core.files import File

from gal_pro.settings import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID
from users.models import User
from gallery.models import Image, ImageS3

from celery import shared_task


@shared_task
def upload_multi_images(unique_id):
    print("Upload")
    img = Image.objects.get(unique_id=unique_id)

    img_images = Image.objects.get(unique_id=unique_id).images

    img_s3 = ImageS3()
    img_s3.unique_id = str(img.unique_id)
    img_s3.images = File(img_images, img_images.name)
    img_s3.gallery_id = img.gallery.id
    img_s3.title = img.title
    img_s3.save()
    img_images.close()
