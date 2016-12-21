from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
# db project_dbsec


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, null=True, blank=True)

    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be entered in the format: '9xxxxxxxxx'. Only 10 integer"
                                         " digits allowed.")
    percentage_regex = RegexValidator(regex=r'^(100|[1-9]?\d\.\d{1}|[1-9]?\d)$',
                                      message="Percentage allowed only in real numbers upto one decimal place.")
    # The additional attributes we wish to include.
    # Basic Profile
    name = models.CharField(max_length=50, blank=True, default=None)
    dob = models.DateField(blank=True,null=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    gender = models.CharField(max_length=1, default=None, blank=True, null=True)
    birthplace = models.CharField(max_length=15, default=None, blank=True, null=True)
    contact = models.CharField(validators=[phone_regex], max_length=10, default=None, blank=True, null=True)
    alternate_contact = models.CharField(validators=[phone_regex], max_length=10, default=None, blank=True, null=True)
    p_up_count = models.IntegerField(default=0, blank=True, null=True)
    s_up_count = models.IntegerField(default=0, blank=True, null=True)
    passphoto = models.CharField(default=None, max_length=250, blank=True, null=True)
    sign = models.CharField(default=None, max_length=250, blank=True, null=True)


    # Current Academic Details
    class_rno = models.IntegerField(default=None, blank=True, null=True)
    univ_rno = models.IntegerField(default=None, blank=True, null=True)
    semester = models.CharField(max_length=1, default=None, blank=True, null=True)
    section = models.CharField(max_length=1, default=None, blank=True, null=True)
    batch = models.CharField(max_length=5, default=None, blank=True, null=True)
    year = models.CharField(max_length=1, default=None, blank=True, null=True)
    branch = models.CharField(max_length=10, default=None, blank=True, null=True)
    college = models.CharField(max_length=100, default=None, blank=True, null=True)

    per_sem1 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem2 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem3 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem4 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem5 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem6 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem7 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    per_sem8 = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)

    # Previous Academic Details
    admission_mode = models.CharField(max_length=10, default=None, blank=True, null=True)
    admission_rank = models.IntegerField(default=None, blank=True, null=True)

    percentage_tenth = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    board_tenth = models.CharField(max_length=10, default=None, blank=True, null=True)
    medium_tenth = models.CharField(max_length=1, default=None, blank=True, null=True)
    year_tenth = models.IntegerField(default=None, blank=True, null=True)
    school_tenth = models.CharField(max_length=150, default=None, blank=True, null=True)

    percentage_twelfth = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    board_twelfth = models.CharField(max_length=10, default=None, blank=True, null=True)
    medium_twelfth = models.CharField(max_length=1, default=None, blank=True, null=True)
    year_twelfth = models.IntegerField(default=None, blank=True, null=True)
    school_twelfth = models.CharField(max_length=150, default=None, blank=True, null=True)

    percentage_diploma = models.CharField(validators=[percentage_regex], max_length=3, default=None, blank=True, null=True)
    stream_diploma = models.CharField(max_length=50, default=None, blank=True, null=True)
    year_diploma = models.IntegerField(default=None, blank=True, null=True)
    college_diploma = models.CharField(max_length=150, default=None, blank=True, null=True)

    # Additional Details
    father_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    father_contact = models.CharField(validators=[phone_regex], max_length=10, default=None, blank=True, null=True)
    father_occupation = models.CharField(max_length=20, default=None, blank=True, null=True)
    mother_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    mother_contact = models.CharField(validators=[phone_regex], max_length=10, default=None, blank=True, null=True)
    mother_occupation = models.CharField(max_length=20, default=None, blank=True, null=True)
    guardian_contact = models.CharField(validators=[phone_regex], max_length=10, default=None, blank=True, null=True)
    present_address = models.CharField(max_length=200, default=None, blank=True, null=True)
    permanent_address = models.CharField(max_length=200, default=None, blank=True, null=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Event(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    by = models.IntegerField()

    def __unicode__(self):
        return self.event_name


class Invite(models.Model):
    eve = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.CharField(max_length=8)


class EventFields(models.Model):
    name = models.BooleanField(default=False)
    dob = models.BooleanField(default=False)
    age = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    contact = models.BooleanField(default=False)
    univ_rno = models.BooleanField(default=False)
    batch = models.BooleanField(default=False)
    father_name = models.BooleanField(default=False)
    mother_name = models.BooleanField(default=False)
    event = models.OneToOneField(Event,null=True, blank=True, default=None, on_delete=models.CASCADE)


class Entries(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile,null=True, blank=True, default=None)

