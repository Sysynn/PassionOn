from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from django.utils import timezone
from datetime import timedelta,datetime
import os

# Create your models here.

class Cloth(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_clothes')
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    price = models.DecimalField(blank=True, max_digits=10, decimal_places=0)
    hits = models.PositiveIntegerField(default=0)


    thumbnail = ProcessedImageField(upload_to='', 
                                    blank=True, processors=[ResizeToFill(400,400)],
                                    format='JPEG',
                                    options={'quality': 100})
    

    gender_choices = (('Male', '남'), ('Female', '여'), ('Unisex', '공용'),)
    gender = models.CharField(max_length=10, choices=gender_choices)
    
    category_choices = (('outer', '아우터'), ('top', '상의'), ('bottom', '하의'), ('cap', '모자'), ('accessories', '악세서리'))
    category = models.CharField(max_length=20, choices=category_choices)

    size_choices = (('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('Free', 'free'))
    size = models.CharField(max_length=15, choices=size_choices)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ClothImage(models.Model):
    cloth = models.ForeignKey(to=Cloth, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='', blank=True,
                                processors=[ResizeToFill(250,300)],
                                format='JPEG',
                                options={'quality': 100})


class Recommend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clothes = models.ManyToManyField(Cloth, related_name='recommendations')
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    hits = models.PositiveIntegerField(default=0)
    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
        

class RecommendImage(models.Model):
    recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='', blank=True,
                                processors=[ResizeToFill(700,900)],
                                format='JPEG',
                                options={'quality': 100})


class Comment(models.Model):
    recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
    

