# Generated by Django 2.2.1 on 2019-05-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_remove_tour_rout'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='DistinationList',
            field=models.TextField(blank=True, null=True),
        ),
    ]
