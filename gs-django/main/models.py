from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=255)
    cnic = models.CharField(max_length=15, unique=True)  # Assuming CNIC is unique for every student
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name