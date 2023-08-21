from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import User
from django.db import models

class PolicePost(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100, blank=False, unique=True)   # name of the police station
    mobile_no = PhoneNumberField(db_column='Mobile No. 1')
    mobile_no_sec = PhoneNumberField(db_column='Mobile No. 2')  # mobile no. 2 - named. 'sec' is short form for secondary
    county = models.CharField(max_length=50, blank=False)
    sub_county = models.CharField(max_length=80, blank=False)
    constituency = models.CharField(max_length=80, blank=False)
    ward = models.CharField(max_length=80, blank=False)
    longitude = models.FloatField(null=True, blank=False)
    latitude = models.FloatField(null=True, blank=False)
    address = models.CharField(max_length=30, blank=False)
    img_file = models.ImageField(upload_to='Stations/', default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['county', 'name']

class OfficerProfile(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    officer = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    police_post = models.ForeignKey(PolicePost, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()
    rank = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.officer}'
    
    class Meta:
        ordering = ['officer', 'police_post']
    