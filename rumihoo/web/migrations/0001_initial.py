# Generated by Django 2.2.1 on 2019-05-20 10:44

from django.db import migrations, models
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Distance', models.IntegerField(blank=True)),
                ('Duration', durationfield.db.models.fields.duration.DurationField()),
                ('Rout', models.ManyToManyField(to='web.Location')),
            ],
        ),
    ]
