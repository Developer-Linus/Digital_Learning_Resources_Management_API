from rest_framework import serializers
from .models import Notification
from resources.models import Resource, Bookmark, LearningLog

# Define notification serializer for serializing and deserializing incoming and outgoing data
class NotificationSerializer(serializers.ModelSerializer):
    target = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'read']
    def get_target(self, instance):
        target = instance.target
        if target:
            if isinstance(target, Resource):
                return {
                    'id': target.id,
                    'type': type(target).__name__,
                    'name': target.resource_name
                }
            elif isinstance(target, LearningLog):
                return {
                    'id': target.id,
                    'type': type(target).__name__,
                    'name': target.resource.resource_name
                }
            elif isinstance(target, Bookmark):
                return {
                    'id': target.id,
                    'type': type(target).__name__,
                    'name': target.resource.resource_name
                }
            else:
                return {
                    'id': target.id,
                    'type': type(target).__name__,
                    'name': str(target)
                }
        return None
            