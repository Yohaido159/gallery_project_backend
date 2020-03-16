# Generated by Django 3.0.3 on 2020-02-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200223_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='gallery_images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.Gallery'),
        ),
    ]
