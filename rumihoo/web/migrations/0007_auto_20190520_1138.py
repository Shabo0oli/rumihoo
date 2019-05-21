# Generated by Django 2.2.1 on 2019-05-20 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190520_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='Excludes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='Includes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='MinPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Caption', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='tourImage/')),
                ('Tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Tour')),
            ],
        ),
    ]