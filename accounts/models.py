from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from clothes.models import Cloth


# Create your models here.
class User(AbstractUser):
    profile_image = ProcessedImageField(blank=True,
                                        upload_to='users',
                                        processors=[ResizeToFill(200, 200)],
                                        format='JPEG',
                                        options={'quality': 70})
    carts = models.ManyToManyField(to=Cloth, through='Cart', related_name='cart_users')
    purchase_logs = models.ManyToManyField(to=Cloth, through='PurchaseLog', related_name='purchase_log_users')
    
    
class Cart(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cloth = models.ForeignKey(to=Cloth, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
class PurchaseLog(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cloth = models.ForeignKey(to=Cloth, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    bought_on = models.DateTimeField(auto_now_add=True)