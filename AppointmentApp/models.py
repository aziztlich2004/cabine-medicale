from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.exceptions import ValidationError



class Status (models.TextChoices):
    pending ='pending','en attente'
    confirmed ='confirmed','confirme'
    cancelled ='cancelled','anunule'

class Appointment(models.Model):
    reason =models.TextField()
    prescription =models.FileField (blank=True,upload_to="prescriptions/",validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    status =models.CharField(max_length=9,choices=Status.choices,default=Status.pending) 
    duration_minutes=models.PositiveIntegerField (default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    appointement_date=models.DateTimeField()
    
    docteur=models.ForeignKey('AccountApp.Docteur',on_delete =models.CASCADE)
    patient = models.ForeignKey('AccountApp.patient',on_delete=models.CASCADE)
    
    


    def clean(self):
            super().clean()

            if self.pk is None:
                if self.appointement_date <= timezone.now():
                    raise ValidationError("date passe")

            else:
                ancienne_date = Appointment.objects.get(pk=self.pk).appointment_date

                if ancienne_date != self.appointment_date:
                    if self.appointment_date <= timezone.now():
                        raise ValidationError("date invalide")    