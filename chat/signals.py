from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Thread, ThreadManager


@receiver(post_save, sender=User)
def chat_thread(sender, instance, created, **kwargs):
    if created:
        Thread.objects.create(user=instance)


