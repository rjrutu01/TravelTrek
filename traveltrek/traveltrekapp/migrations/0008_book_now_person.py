# Generated by Django 5.0.7 on 2024-07-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltrekapp', '0007_book_now_total_price_alter_destination_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_now',
            name='person',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
