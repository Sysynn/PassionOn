from django.db import models
from django.conf import settings
from clothes.models import Cloth
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    rating = models.IntegerField()
    
    def star_rating(self):
        return '⭐' * self.rating
    
    def empty_stat_rating(self):
        return '☆' * (5 - self.rating)

    created_at = models.DateTimeField(auto_now_add=True)


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='', blank=True,
                                processors=[ResizeToFill(100,100)],
                                format='JPEG',
                                options={'quality': 80})