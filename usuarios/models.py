from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(unique=True)  #unique=True → não permite emails repetidos
    senha = models.CharField(max_length=100) 

    def __str__(self):
        return self.email
