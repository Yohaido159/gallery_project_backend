# Generated by Django 3.0.3 on 2020-03-10 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0018_auto_20200310_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='unique_i',
        ),
    ]