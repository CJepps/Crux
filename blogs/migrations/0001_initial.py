# Generated by Django 3.2 on 2022-03-21 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_caption', models.CharField(blank=True, max_length=60, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subheading1', models.CharField(blank=True, max_length=60, null=True)),
                ('para1', models.TextField()),
                ('subheading2', models.CharField(blank=True, max_length=60, null=True)),
                ('para2', models.TextField(blank=True, null=True)),
                ('subheading3', models.CharField(blank=True, max_length=60, null=True)),
                ('para3', models.TextField(blank=True, null=True)),
                ('subheading4', models.CharField(blank=True, max_length=60, null=True)),
                ('para4', models.TextField()),
                ('subheading5', models.CharField(blank=True, max_length=60, null=True)),
                ('para5', models.TextField(blank=True, null=True)),
                ('subheading6', models.CharField(blank=True, max_length=60, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
