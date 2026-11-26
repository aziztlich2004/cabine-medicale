from django.contrib import admin
from .models import Docteur, Patient, Specialite

admin.site.register(Docteur)
admin.site.register(Patient)
admin.site.register(Specialite)
