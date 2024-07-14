from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length= 100)
    second_name = models.CharField(max_length= 100)
    email = models.EmailField()
    bio = models.TextField() 
    bday = models.DateField()


    def __str__(self):
        return f'{self.name} {self.second_name}'
