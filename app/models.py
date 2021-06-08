from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
# Create your models here.

    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    id          = models.AutoField(primary_key=True)
    email       = models.EmailField("Email Adress",unique=True)
    is_car      = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= []
    object = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    

class Location(models.Model):
    
    car       =models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    longitude =models.FloatField(validators=
                                [MinValueValidator(-180,message="value must be in range [-180,180]"),
                                 MaxValueValidator(180,message="value must be in range [-180,180]")])
    latitude  =models.FloatField(validators=
                                [MinValueValidator(-90,message="value must be in range [-90,90]"),
                                 MaxValueValidator(90,message="value must be in range [-90,90]")])
    timestamp =models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self):
        return "longitude :"+str(self.longitude)+" latitude :"+str(self.latitude)
    
    
    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)
        
        
        
    def validate_longitude(self):
            if self.longitude<-180 or self.longitude>180:
                return False
            else:
                return True

    def validate_latitude(value):
            if self.latitude<=-90 or self.latitude>=90:
                return False
            else:
                return True

            