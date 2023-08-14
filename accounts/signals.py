from django.db.models.signals import pre_save
from .models import User, OfficerProfile
from django.dispatch import receiver
from datetime import datetime
import uuid

@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.date_joined.strftime('%Y-%m-%d %H:%M:%S'):
            user_dob = str(instance.dob)
            get_user_dob = datetime.strptime(user_dob, '%Y-%m-%d')
            current_date = datetime.now()
            user_age = current_date - get_user_dob
            convert_user_age = int(user_age.days/365.25)
            instance.age = convert_user_age
            
        else:
            user_dob = str(instance.dob)
            get_user_dob = datetime.strptime(user_dob, '%Y-%m-%d')
            current_date = datetime.now()
            user_age = current_date - get_user_dob
            convert_user_age = int(user_age.days/365.25)
            instance.age = convert_user_age
    
    except AttributeError:
        return

@receiver(pre_save, sender=OfficerProfile)
def generate_officialsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]
