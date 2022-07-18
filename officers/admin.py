from django.contrib import admin
from .models import OfficialsProfile, CrimeReported, WantedSuspect

admin.site.register(OfficialsProfile)
admin.site.register(CrimeReported)
admin.site.register(WantedSuspect)
