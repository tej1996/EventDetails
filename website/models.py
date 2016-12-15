from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: ' + self.name


class Events(models.Model):
    event_name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

