from django.db.models.signals import post_save # check for the action (sending Post_save signals)
from django.contrib.auth.models import User
from django.dispatch import receiver # reveiving the signals
from .models import Profile


@receiver(post_save, sender = User)
def build_profile(sender,instance,created,**kwargs):      # sender : which sends signals / instance = instance which is being saved/ created : boolean value 
    if created:     # If user is created 
        Profile.objects.create(user=instance)        


@receiver(post_save, sender = User)
def save_profile(sender,instance,**kwagrs):
    instance.profile.save()
