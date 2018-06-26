# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-25 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='posts/')),
                ('name', models.CharField(max_length=30)),
                ('post', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, null=True)),
                ('last_name', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, upload_to='avatar')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('category', models.CharField(choices=[('CL', 'Criminal'), ('CE', 'Corporate'), ('FL', 'Financial'), ('ET', 'Entertainment'), ('FY', 'Family'), ('EL', 'Enviromental'), ('AY', 'Admiralty'), ('GN', 'General')], default='GN', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyer.Lawyer'),
        ),
    ]
