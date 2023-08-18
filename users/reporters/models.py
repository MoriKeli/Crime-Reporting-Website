from accounts.models import User
from django.db import models
from PIL import Image

class CrimeRecords(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    description = models.TextField(blank=False)
    dt_crime = models.DateTimeField(null=True, blank=False, db_column='Datetime of crime')
    county = models.CharField(max_length=20, blank=False)
    sub_county = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=70, blank=False)
    type_of_crime = models.CharField(max_length=30, blank=False)
    media_file = models.FileField(upload_to='Evidences/Files/', blank=True)
    reported = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reported_by}'
    
    class Meta:
        ordering = ['-reported', '-dt_crime']

