# Generated by Django 2.2.1 on 2019-06-18 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20190618_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='Accomodation',
            field=models.ManyToManyField(blank=True, null=True, to='web.Accomodation'),
        ),
        migrations.AddField(
            model_name='destination',
            name='Climate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='Distance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='Language',
            field=models.ManyToManyField(blank=True, null=True, to='web.Language'),
        ),
        migrations.AddField(
            model_name='destination',
            name='Meal',
            field=models.ManyToManyField(blank=True, null=True, to='web.Meal'),
        ),
        migrations.AddField(
            model_name='destination',
            name='Population',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='ReviewText',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='Transport',
            field=models.ManyToManyField(blank=True, null=True, to='web.Transport'),
        ),
        migrations.AddField(
            model_name='destination',
            name='Type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='WhereToEat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='UnescoSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='MustSee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='LocalFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Handicraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='web/static/image/DistImage/')),
                ('Destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Destination')),
            ],
        ),
    ]
