# Generated by Django 3.2.7 on 2021-09-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_remove_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
