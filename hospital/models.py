from django.db import models
from tinymce.models import HTMLField  
from autoslug import AutoSlugField
from django.utils import timezone
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    image = models.ImageField(upload_to='department', null=True)
    name = models.CharField(max_length=200)
    description = HTMLField()
    d_slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class EducationalQualification(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField()
    start_year = models.DateField(null=True)
    end_year = models.DateField(null=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}-{self.start_year}-{self.end_year}"


DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
class DoctorSchedule(models.Model):
    day_of_week = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(null=True, blank=True)  
    end_time = models.TimeField(null=True, blank=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.end_time if self.start_time and self.end_time else 'Closed'}"

class Expertise(models.Model):
    name = models.CharField(max_length=200)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.name} - {self.doctor.name}"
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='doctor')
    specialist = models.CharField(max_length=200)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    slug = AutoSlugField(populate_from='name',null=True)

    def __str__(self):
        return f"{self.name} - {self.specialist}"
    


class Appointment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time}"