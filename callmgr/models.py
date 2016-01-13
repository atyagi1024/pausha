from __future__ import unicode_literals
from django.db import models


from django.db import models

# Create your models here.


class Apex(models.Model):
    apex_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.apex_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_mobile = models.CharField(max_length=15)
    phone_fixed = models.CharField(max_length=15)
    email_id = models.EmailField()
    apex = models.ForeignKey(Apex)
    Remarks = models.TextField()

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Location(models.Model):
    location_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.location_name

class Program(models.Model):
    program_name = models.CharField(max_length=20)
    program_date = models.DateField()
    program_location = models.ForeignKey(Location)
    program_details = models.TextField()