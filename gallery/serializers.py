import demjson

from rest_framework import serializers
from .models import Gallery, Image, ImageS3


from upload.tasks import upload_multi_images

from django.conf import settings


class SerializerImages(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ("unique_id", "images", "title")

    def to_representation(self, instance):
        representation = super(SerializerImages, self).to_representation(instance)
        domain_name = settings.DOMIN
        full_path = "http://" + domain_name + instance.images.url
        representation['images'] = full_path
        return representation


class SerializerImagesS3(serializers.ModelSerializer):
    class Meta:
        model = ImageS3
        fields = ("unique_id", "images", "title",)


class SerializerGallery(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


# route
class SerializerGalleryImages(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    images = SerializerImages(many=True)
    images_s3 = SerializerImagesS3(many=True, required=False)

    class Meta:
        model = Gallery
        fields = "__all__"

    def create(self, validated_data):
        images = validated_data.pop("images")
        gallery, b = Gallery.objects.get_or_create(title=validated_data.get("title"))

        for image in images:
            img = Image.objects.create(gallery_id=gallery.id, **image)
            # upload_multi_images.delay(img.unique_id)
        return gallery

    def to_representation(self, instance):
        representation = super(SerializerGalleryImages, self).to_representation(instance)
        domain_name = settings.DOMIN
        full_path = "http://" + domain_name + instance.image_gallery.url
        representation['image_gallery'] = full_path
        return representation
