from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    """ This model maps and stores common user profile attributes. The model extends from AbstractUser class. """
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=7, blank=False)
    dob = models.DateField(null=True, blank=False, db_column='date of birth')
    age = models.PositiveIntegerField(default=0, editable=False)
    mobile_no = PhoneNumberField()
    county = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=70, blank=False)
    town = models.CharField(max_length=70, blank=False)
    profile_pic = models.ImageField(upload_to='Users-Dps/', default='default.png')
    is_crimereporter = models.BooleanField(default=False, editable=False)
    is_officer = models.BooleanField(default=False, editable=False)
    edited = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    # override save() to resize user's profile picture.
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)
        if img.height > 400 and img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    class Meta:
        ordering = ['first_name', 'last_name', '-edited']

class OfficerProfile(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()
    police_post = models.CharField(max_length=70, blank=False)
    rank = models.CharField(max_length=50, blank=False)
    mobile_no_1 = PhoneNumberField()
    mobile_no_2 = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Officers'

