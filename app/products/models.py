from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .utils import extract_features

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    features = models.BinaryField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - ${self.price}"

@receiver(post_save, sender=Product)
def extract_product_features(sender, instance, **kwargs):
    if not instance.features:
        features = extract_features(instance.image.path)
        if features:
            instance.features = features
            instance.save(update_fields=['features'])