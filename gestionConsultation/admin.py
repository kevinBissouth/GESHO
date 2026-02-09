from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Patient, Medecin, Specialite, Consultation

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Specialite)
admin.site.register(Consultation)