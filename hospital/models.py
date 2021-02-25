from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def save_patient(self):
        self.save()

class Hospital(models.Model):
    name = models.CharField(max_length=20)

class Department(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=600)
    department_image = models.ImageField(upload_to='departments/',blank=True)
    # hospitals = models.ForeignKey(Hospital,on_delete=models.CASCADE)

    def save_department(self):
        self.save()

    def delete_department(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def search_departments(cls, search_term):
        return cls.objects.filter(Q(name__icontains = search_term)|Q(description__icontains = search_term))

    def get_department_doctors(self):
        return self.doctors.all


class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    details = models.CharField(max_length=600)
    doctor_image = models.ImageField(upload_to='doctors/',blank=True)
    departments = models.ForeignKey(Department,on_delete=models.CASCADE)

    def save_doctor(self):
        self.save()


    def __str__(self):
        return self.first_name

class Schedule(models.Model):
    app_date = models.DateField()
    app_hour = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True)

    def save_schedule(self):
        self.save()

    def delete_schedule(self):
        self.delete()

    @classmethod
    def get_schedule_by_doctor(cls, doctor_id):
        return cls.objects.filter(doctor = doctor_id).all()

class Appointment(models.Model):
    doctors = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patients = models.ForeignKey(Patient,on_delete=models.CASCADE)
    schedules = models.ForeignKey(Schedule,on_delete=models.CASCADE,default='1')

    def save_appointment(self):
        self.save()
