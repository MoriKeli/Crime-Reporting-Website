from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import UserProfile
from datetime import datetime
import uuid

@receiver(pre_save, sender=UserProfile)
def calculate_age(sender, instance, **kwargs):
    try:
        if  datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
            user_dob = str(instance.dob)
            strip_dob = datetime.strptime(user_dob, '%Y-%m-%d')
            current_date = datetime.now()
            new_user_age = current_date - strip_dob
            convert_age = int(new_user_age.days/365.25)
            instance.age = convert_age
        
        else:
            user_dob = str(instance.dob)
            strip_dob = datetime.strptime(user_dob, '%Y-%m-%d')
            current_date = datetime.now()
            new_user_age = current_date - strip_dob
            convert_age = int(new_user_age.days/365.25)
            instance.age = convert_age
        
    except AttributeError:
        return

@receiver(pre_save, sender=UserProfile)
def generate_user_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "")[:13]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            UserProfile.objects.create(reporter=instance)


