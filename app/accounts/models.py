from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png'
    )
    
    def get_absolute_url(self):
        return reverse('profile')
    
    def __str__(self):
        return self.username