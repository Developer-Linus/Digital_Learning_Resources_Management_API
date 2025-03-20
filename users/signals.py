from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUser, Profile

# Signal to create a profile when a user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(self, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save a profile when a user is updated
@receiver(post_save, sender=CustomUser)
def save_user_profile(self, instance, **kwargs):
    instance.profile.save() # Save the linked profile

# Signal to delete a profile when a user deletes account
@receiver(post_delete, sender=CustomUser)
def delete_user_profile(self, instance, **kwargs):
    instance.profile.delete()

