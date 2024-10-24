
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  name=models.CharField(max_length=255)
  address=models.CharField(max_length=255)
  phone_number=models.CharField(max_length=255)
  gender=models.CharField(max_length=255)
