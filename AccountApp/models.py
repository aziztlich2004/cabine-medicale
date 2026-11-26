from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator 
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_past_date(value):
    if value >= timezone.localdate():
        return False
    else:
        return True


class User(AbstractUser):
    pass

class Specialite(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
class Docteur(User):
    licence_number=models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6)])
    phone_number=models.CharField(max_length=8,unique=True,validators=[RegexValidator(regex=(r"^\d{8}$"),message="le num de tel est non valide")])

    Specialite=models.ManyToManyField(Specialite,related_name="Docteur")
    def __str__(self):
        return "{self.first_name}{self.last_name}"


class Patient (User):
    national_id=models.CharField(max_length=8,unique=True,validators=[MinLengthValidator(8)])    
    phone=models.CharField(max_length=8,validators=[RegexValidator(regex=(r'^\d{8}$'),message="num incorrecte")])
    birth_date=models.DateField(validators=[validate_past_date])

    
    def __str__(self):
        return "{self.first_name}{self.last_name}"

    def clean(self):
        super().clean()
        if validate_past_date(self.birth_date)==False:
            raise ValidationError("date")



    
