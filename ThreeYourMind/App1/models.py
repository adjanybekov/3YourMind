from django.db import models

# Create your models here.
class Profile(models.Model):
    myfile = models.FileField(upload_to='media/')