from django.db import models

class Project(models.Model):
	image = models.ImageField(upload_to='images/')
	character = models.CharField(max_length=100)
# Create your models here.
