from django.db import models

from users.models import User

import uuid


from storages.backends.s3boto3 import S3Boto3Storage
from gal_pro.storage_backends import MediaStorage


def get_users_gallery(instance, filename):
    user = instance.gallery.user.email
    gallery = instance.gallery.title
    return "galleries/%s/%s/%s" % (user, gallery, filename)


def get_galleries_image(instance, filename):
    if instance.user:
        email = instance.user.email
        return "galleries/%s/%s" % (email, filename)
    return "unknow/%s" % (filename)


class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Galleries"

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    image_gallery = models.ImageField(
        upload_to=get_galleries_image, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    type_photography = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    is_copyright = models.CharField(max_length=50, blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title or ""

    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)
        if self.title is None:
            return Gallery.objects.filter(id=self.id).update(title=f"Gallery_{self.id}")
        return Gallery.objects.get(id=self.id)


class Image(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    images = models.ImageField(upload_to=get_users_gallery, blank=True, null=True)

    title = models.CharField(max_length=50, blank=True, null=True)

    description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.title is not None:
            return self.title
        return "non title"

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        # if self.title is None:
        #     Image.objects.filter(id=self.id).update(
        #         title=f"{self.gallery.title}_{self.id}")
        return Image.objects.get(id=self.id)


class ImageS3(models.Model):
    unique_id = models.CharField(max_length=100, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, related_name='images_s3', on_delete=models.CASCADE, blank=True, null=True)
    images = models.ImageField(upload_to=get_users_gallery, storage=MediaStorage(), blank=True, null=True)

    title = models.CharField(max_length=50, blank=True, null=True)

    description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.title is not None:
            return self.title
        return "non title"
