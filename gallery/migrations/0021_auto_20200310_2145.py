
from django.db import migrations, models
import uuid

from gallery.models import Image


def create_uuid(apps, schema_editor):
    images = Image.objects.all()
    for image in images:
        image.unique_id = uuid.uuid4()
        image.save()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0020_auto_20200310_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='unique_id',
            field=models.UUIDField(
                blank=True, null=True, primary_key=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='image',
            name='unique_id',
            field=models.UUIDField(
                default=uuid.uuid4, unique=True,  blank=True, null=True, primary_key=True)
        )
    ]
