# Generated by Django 5.0.7 on 2024-07-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltrekapp', '0002_rename_desc_destination_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='img',
        ),
        migrations.AddField(
            model_name='destination',
            name='image',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
    ]