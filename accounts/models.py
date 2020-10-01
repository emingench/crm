from django.db import models

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    email= models.EmailField( max_length=254)
    date_created = models.DateTimeField(auto_now_add)