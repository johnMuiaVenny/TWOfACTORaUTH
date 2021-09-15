from .models import CODE, CUSTOMUSER
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CUSTOMUSER)
def GenerateCode(sender, instance, created, *args, **kwargs):
    if created:
        CODE.objects.create(user=instance)