# Generated by Django 3.2.18 on 2023-05-15 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes', '0002_auto_20230511_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=200)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
                ('clothes', models.ManyToManyField(related_name='recommendations', to='clothes.Cloth')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]