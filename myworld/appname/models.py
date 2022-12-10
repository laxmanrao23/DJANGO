from django.db import models

# Create your models here.
class Member(models.Model):
        First_Name = models.CharField(max_length=50)
        Last_Name = models.CharField(max_length=50)
        DOB = models.DateField()
        dropdown = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        password = models.CharField(max_length=50)
        phone = models.IntegerField(max_length=10)

        def __str__(self):
            return self.First_Name+' '+self.Last_Name

        

