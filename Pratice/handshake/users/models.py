from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # If we delete user Profile will get deleted 
    images = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('users:post-detail', kwargs={'pk':self.pk})




