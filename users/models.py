from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=13)
    reporter = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=14)
    dob = models.DateField(null=True)
    age = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.reporter.username}'
    
    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['reporter']
        
