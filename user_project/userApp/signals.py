from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from userApp.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile associated with a User.
    """
    if created:
        user_profile = Profile.objects.create(user=instance, full_name='', cnic='',
                                                        contact_number='', address='' )
        user_profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Saves Profile data associated with a User.
    """
    instance.profile.save()
