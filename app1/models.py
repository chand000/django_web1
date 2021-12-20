from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()


# this value save in main user 
class Signup(models.Model):
    # username = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = EmailField(max_length=254)
    password = models.TextField()
    # repassword = models.TextField()
