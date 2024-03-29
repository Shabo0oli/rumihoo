# Generated by Django 2.2.1 on 2019-05-21 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_tour_mainimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='MainImage',
            field=models.ImageField(blank=True, null=True, upload_to='../web/static/image/tourImage/'),
        ),
        migrations.AlterField(
            model_name='tourimage',
            name='Image',
            field=models.ImageField(upload_to='../web/static/image/tourImage/'),
        ),
    ]
