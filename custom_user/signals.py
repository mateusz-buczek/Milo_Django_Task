from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import random


# using django signals, profile with random number is created after user creation(and saving)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        profile = Profile.objects.get(user=instance)
        profile.random_number = random.randint(1, 100)
        profile.save()




