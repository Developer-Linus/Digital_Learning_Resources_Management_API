from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUser, Profile

# Signal to create a profile when a normal user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:  # Ensure profile is not created for superusers
        profile = Profile.objects.create(user=instance)
        profile.save()

# Signal to save a profile when a user is updated
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    #Save profile only if it exists
    if hasattr(instance, 'profile'):
        instance.profile.save() # Save the linked profile

# Signal to delete a profile when a user deletes account
@receiver(post_delete, sender=CustomUser)
def delete_user_profile(sender, instance, **kwargs):
    instance.profile.delete()

