# Generated by Django 2.2.1 on 2019-07-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenttour',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]