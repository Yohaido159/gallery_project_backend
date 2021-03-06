# Generated by Django 3.0.3 on 2020-03-03 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_imagecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(blank=True, max_length=50, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='imagecomment',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='ImageComment',
        ),
    ]
