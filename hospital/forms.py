from django import forms
from .models import Patient, Hospital, Doctor, Schedule, Department, Appointment
from tinymce.widgets import TinyMCE

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name","description",)
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control mb-4"}),
            "description":TinyMCE(attrs={'cols': 116, 'rows': 15}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ("first_name","last_name","email","phone_number","details","doctor_image","departments",)
        # exclude = ['departments']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['app_date', 'app_hour','doctor']

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name","description",)