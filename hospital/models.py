from django.db import models

# Create your models here.
Hours=(
    ('10:00am - 11:00am','10:00am - 11:00am'),
    ('11:00am - 12:00pm','11:00am - 12:00pm'),
    ('2:00pm - 3:00pm','2:00pm - 3:00pm'),
    ('3:00pm - 4:00pm','3:00pm - 4:00pm'),

)
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField()

class Hospital(models.Model):
    name = models.CharField(max_length=20)

class Department(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=600)
    hospitals = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    details = models.CharField(max_length=600)
    doctor_image = models.ImageField(upload_to='images/')
    departments = models.ForeignKey(Department,on_delete=models.CASCADE)

class Appointment(models.Model):
    app_date = models.DateTimeField()
    app_hour = models.CharField(max_length=20,choices=Hours,default="10:00am - 11:00am")
    doctors = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patients = models.ForeignKey(Patient,on_delete=models.CASCADE) 



