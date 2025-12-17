from django.db import models

# class Usuario(models.Model): 
    # nome = models.CharField(max_length=100) 
    #email = models.EmailField() 
# Create your models here.

class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email
