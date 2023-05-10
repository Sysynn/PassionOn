from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
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
                                    blank=True, processors=[ResizeToFill(300,300)],
                                    format='JPEG',
                                    options={'quality': 100})
    

    gender_choices = (('Male', '남'), ('Female', '여'), ('Unisex', '공용'),)
    gender = models.CharField(max_length=10, choices=gender_choices)
    
    category_choices = (('outer', '아우터'), ('top', '상의'), ('bottom', '하의'), ('shoes', '신발'), ('cap', '모자'), ('accessories', '악세서리'))
    category = models.CharField(max_length=10, choices=category_choices)

    size_choices = (('Small', 'S'), ('Medium', 'M'), ('Large', 'L'),)
    size = models.CharField(max_length=10, choices=size_choices)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ClothImage(models.Model):
    cloth = models.ForeignKey(to=Cloth, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='', blank=True,
                                processors=[ResizeToFill(300,300)],
                                format='JPEG',
                                options={'quality': 100})