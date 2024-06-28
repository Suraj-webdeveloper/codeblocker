from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=122)
    password= models.CharField(max_length=12)
    phonenumber = models.CharField(max_length=12, default=1)
    city = models.CharField(max_length=20, default="foobar")
    state = models.CharField(max_length=20, default="foobar")