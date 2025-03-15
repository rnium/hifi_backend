from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import FeedBack, Notification

User = get_user_model()

@receiver(post_save, sender=FeedBack)
def create_feedback_notification(sender, instance, created, **kwargs):
    if created:
        staff_users = User.objects.filter(is_staff=True)
        for user in staff_users:
            Notification.objects.create(
                user=user,
                message=f"New feedback from {str(instance.user)}",
                n_type="feedback",
                related_id=instance.id
            )