# Generated by Django 5.0.7 on 2024-07-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltrekapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='desc',
            new_name='description',
        ),
        migrations.AddField(
            model_name='destination',
            name='category',
            field=models.CharField(choices=[('adventure', 'adventure'), ('wildlife', 'wildlife'), ('beach', 'beach')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
