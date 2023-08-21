from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import PolicePost, OfficerProfile
from uuid import uuid4

@receiver(pre_save, sender=PolicePost)
def generate_policepostID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=OfficerProfile)
def generate_officerID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:25]
