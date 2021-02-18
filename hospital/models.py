from django.db import models

# Create your models here.
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

class Schedule(models.Model):
    app_date = models.DateField()
    app_hour = models.CharField(max_length=30)

class Appointment(models.Model):
    doctors = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patients = models.ForeignKey(Patient,on_delete=models.CASCADE)
    schedules = models.ForeignKey(Schedule,on_delete=models.CASCADE,default='1')




