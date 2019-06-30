# Generated by Django 2.2.1 on 2019-06-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_tour_googlemap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
            ],
        ),
    ]