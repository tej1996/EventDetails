from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: ' + self.name

