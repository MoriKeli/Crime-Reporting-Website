from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from officers.models import CrimeReported, OfficialsProfile, WantedSuspect
from datetime import datetime
import uuid

@receiver(pre_save, sender=OfficialsProfile)
def calculate_officer_age(sender, instance, **kwargs):
    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
            officer_dob = str(instance.dob)
            strip_dob = datetime.strptime(officer_dob, '%Y-%m-%d')
            current_date = datetime.now()
            officer_age = current_date - strip_dob
            convert_age = int(officer_age.days/365.25)
            instance.age = convert_age
        
        else:
            officer_dob = str(instance.dob)
            strip_dob = datetime.strptime(officer_dob, '%Y-%m-%d')
            current_date = datetime.now()
            new_user_age = current_date - strip_dob
            convert_age = int(new_user_age.days/365.25)
            instance.age = convert_age
            print(f'Except:-> Age: {instance.age}')
    
    except AttributeError:
        return


@receiver(pre_save, sender=OfficialsProfile)
def generate_officer_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name='id')).replace("-", "").upper()[:12]


@receiver(post_save, sender=User)
def create_officer_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is True and instance.is_superuser is False:
            OfficialsProfile.objects.create(officer=instance)

@receiver(pre_save, sender=CrimeReported)
def generate_case_file_code(sender, instance, **kwargs):
    if instance.case_file_no == "":
        instance.case_file_no = str(uuid.uuid4()).replace("-", "").upper()[:15]


@receiver(pre_save, sender=WantedSuspect)
def generate_suspect_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "").upper()[:15]
   