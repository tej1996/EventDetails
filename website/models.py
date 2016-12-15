from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, null=True, blank=True)

    # The additional attributes we wish to include.
    name = models.CharField(max_length=50, default=None)
    age = models.IntegerField(default=None, blank=True, null=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Events(models.Model):
    event_name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    by = models.IntegerField(default=23)
