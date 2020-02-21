from django.db.models.signals import post_save   # Sending POST_SAVE signals
from django.contrib.auth.models import User
from django.dispatch import receiver    # It will receive send signals and perform some action 
from .models import Profile


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs): 
    # '''instance =  Instance which is being saved (instance = User) Jo action perform hoga like "User save hone pe" 
    #                                                         Created = Boolean value (User is created or Not True/False)
    #                                                         **kwargs = Any additional fields '''
    if created:
        Profile.objects.create(user = instance)



@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        