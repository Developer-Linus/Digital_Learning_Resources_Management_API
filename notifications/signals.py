from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import Notification
from resources.models import Resource, LearningLog, Bookmark
from .utils import Util


# Define signal for new resources
@receiver(post_save, sender=Resource)
def create_resource_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification for user who added the resource
        Notification.objects.create(
            recipient=instance.owner,
            actor=instance.owner,
            verb='added',
            target=instance
        )
        Util.send_notification_email(instance.owner, f'{instance.owner.email} added a new resource: {instance.resource_name}')

# Define signal receiver for bookmarked resource
@receiver(post_save, sender=Bookmark)
def create_bookmark_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.owner,
            actor=instance.owner,
            verb='bookmarked',
            target=instance
        )
        Util.send_notification_email(instance.owner, f'{instance.owner.email} bookmarked a resource: {instance.resource.resource_name}')

# Define signal receiver for creating a learning log
@receiver(post_save, sender=LearningLog)
def create_learning_log(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.owner,
            actor=instance.owner,
            verb='created a learning log',
            target=instance
        )
        Util.send_notification_email(instance.owner, f'{instance.owner.email} created a learning log for: {instance.resource.resource_name}')