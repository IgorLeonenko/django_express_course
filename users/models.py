from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
