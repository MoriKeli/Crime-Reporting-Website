from .models import PolicePosts, SuspectsRecords
from django.db.models.signals import pre_save
from django.dispatch import receiver
from uuid import uuid4

@receiver(pre_save, sender=PolicePosts)
def generate_policepostID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=SuspectsRecords)
def generate_suspectID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:25]
