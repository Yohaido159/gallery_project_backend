# Generated by Django 3.0.3 on 2020-03-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_utils_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_created',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
