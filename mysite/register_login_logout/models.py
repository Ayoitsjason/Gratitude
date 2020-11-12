from django.db import models

# Create your models here.
class UserForm(models.Model):
    firstname = models.CharField("First Name", max_length=150)
    lastname = models.CharField("Last Name", max_length = 150)
    email = models.EmailField("Email")
    username = models.CharField("Username", max_length=16)
    password = models.CharField("Password", max_length=16)
