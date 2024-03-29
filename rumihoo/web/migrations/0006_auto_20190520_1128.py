# Generated by Django 2.2.1 on 2019-05-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20190520_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='MaxGroupSize',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='MinGroupSize',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='Overview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='PhysicalRate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Text', models.TextField(blank=True, null=True)),
                ('Highlight', models.TextField(blank=True, null=True)),
                ('Tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='Accomodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Accomodation'),
        ),
        migrations.AddField(
            model_name='tour',
            name='Language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Language'),
        ),
        migrations.AddField(
            model_name='tour',
            name='Meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Meal'),
        ),
        migrations.AddField(
            model_name='tour',
            name='Transport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Transport'),
        ),
    ]
