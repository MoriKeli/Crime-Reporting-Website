from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class OfficialsProfile(models.Model):
    id = models.CharField(primary_key=True, editable=False, unique=True, max_length=12)
    officer = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    officer_no = models.CharField(max_length=30, blank=False, unique=True)
    police_post = models.CharField(max_length=30, blank=False)
    rank = models.CharField(max_length=30, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    dp = models.ImageField(upload_to='Officer-Dps', default='officer.png', blank=False)
    gender = models.CharField(max_length=7, blank=False)
    dob = models.DateField(null=True, blank=False)
    age = models.PositiveIntegerField(default=0)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        super(OfficialsProfile, self).save(*args, **kwargs)
        
        image = Image.open(self.dp.path)
        
        if image.height > 500 and image.width > 500:
            output_size = (500, 500)
            image.thumbnail(output_size)
            image.save(self.dp.path)
            

    def __str__(self):
        return f'{self.officer}'
    
    class Meta:
        verbose_name_plural = 'Officials'
        ordering = ['officer']


class CrimeReported(models.Model):
    reported_by = models.CharField(max_length=100, editable=False)
    case_file_no = models.CharField(primary_key=True, editable=False, unique=True, max_length=17)
    suspect_name = models.CharField(max_length=100)
    type_of_crime = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    date_of_crime = models.DateTimeField(blank=False)
    crime_status = models.CharField(max_length=50, blank=False)
    
    crime_reported = models.DateTimeField(auto_now_add=True)
    status_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Crimes Reported'
        
    def __str__(self):
        return f'{self.location}'
    

class WantedSuspect(models.Model):
    id = models.CharField(max_length=15, unique=True, primary_key=True, editable=False)
    suspect_pic = models.ImageField(upload_to='Suspects-Images/', default='criminal.jpg')
    suspect_name = models.CharField(max_length=150, blank=False)
    alias = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=7, blank=False)
    crime = models.CharField(max_length=100, blank=False)
    bounty = models.PositiveIntegerField(default=0, blank=True)
    last_seen = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20)
    
    reported = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  
    
    def save(self, *args, **kwargs):
        super(WantedSuspect, self).save(*args, **kwargs)
        
        suspect_img = Image.open(self.suspect_pic.path)
        
        if suspect_img.height > 300 and suspect_img.width > 300:
            output_size = (500, 500)
            suspect_img.thumbnail(output_size)
            suspect_img.save(self.suspect_pic.path)
        
    def __str__(self):
        return f'{self.suspect_name}'
    

class OccurenceBook(models.Model):
    id  = models.DateField(primary_key=True, editable=False, auto_now_add=True)
    police_station = models.CharField(max_length=100)
    activity = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}'

