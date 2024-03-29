# Generated by Django 4.0.4 on 2022-10-22 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('shift', models.CharField(max_length=122, null=True)),
                ('potNumber', models.IntegerField(blank=True, null=True)),
                ('bathTemperature', models.IntegerField(blank=True, null=True)),
                ('recommendedValue', models.IntegerField(blank=True, null=True)),
                ('recommendationStatus', models.CharField(max_length=122, null=True)),
                ('setValue', models.IntegerField(blank=True, null=True)),
                ('notFollowedReason', models.TextField(max_length=122, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usertags',
            name='user',
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='UserTags',
        ),
    ]
