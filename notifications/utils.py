from django.core.mail import EmailMessage
from django.conf import settings

class Util:
    @staticmethod
    # Define send_notification_email function
    def send_notification_email(recipient, message):
        email = EmailMessage(
            subject='Notification from Digital Learning Resource Management API',
            body=message,
            to=[recipient.email]
        )
        email.send(fail_silently=False)
    