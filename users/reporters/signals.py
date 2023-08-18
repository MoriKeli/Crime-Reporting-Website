from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CrimeRecords
import uuid

@receiver(pre_save, sender=CrimeRecords)
def generate_recordID(self, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]
