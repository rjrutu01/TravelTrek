# Generated by Django 5.0.7 on 2024-07-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltrekapp', '0003_remove_destination_img_destination_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='hotel_image')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(upload_to='destination_image'),
        ),
    ]
