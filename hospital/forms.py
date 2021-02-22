from django import forms
from .models import Patient, Hospital, Doctor, Schedule, Department, Appointment

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['hospitals']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['departments']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['app_date', 'app_hour']