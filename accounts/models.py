from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=7, blank=False)
    dob = models.DateField(null=True, blank=False, db_column='Date of Birth')
    age = models.PositiveIntegerField(default=0, editable=False)
    phone_no = models.CharField(max_length=14, blank=False)
    profile_pic = models.ImageField(upload_to='Users-Dps/', default='default.png')
    edited = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

    class Meta:
        ordering = ['first_name', 'last_name', '-created']
        