# Generated by Django 2.2.1 on 2019-05-21 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190520_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='MainImage',
            field=models.ImageField(blank=True, null=True, upload_to='tourImage/'),
        ),
    ]