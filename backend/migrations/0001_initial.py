# Generated by Django 4.2.7 on 2023-12-06 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_id', models.IntegerField(unique=True)),
                ('fetched', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('by', models.CharField(max_length=255)),
                ('descendants', models.IntegerField()),
                ('score', models.IntegerField()),
                ('text', models.TextField()),
                ('type', models.CharField(default='story', max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField(unique=True)),
                ('by', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('type', models.CharField(default='comment', max_length=20)),
                ('time', models.DateTimeField()),
                ('parent_story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='backend.story')),
            ],
        ),
    ]
