from django.db import models


class Member2(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name
