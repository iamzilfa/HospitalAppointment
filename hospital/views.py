from django.shortcuts import render
from .forms import DepartmentForm, DoctorForm, ScheduleForm

def index(request):
    return render(request, 'index.html')

def new_department(request):
    departform = DepartmentForm()
    return render(request, 'admin/new-department.html', {'form': departform})

def all_departments(request):
    return render(request, 'admin/all-departments.html')

def new_doctor(request):
    doctorform = DoctorForm()
    return render(request, 'admin/new-doctor.html', {'form': doctorform})

def all_doctors(request):
    return render(request, 'admin/all-doctors.html')

def new_schedule(request):
    scheduleform = ScheduleForm()
    return render(request, 'admin/new-schedule.html', {'form': scheduleform})

def all_schedules(request):
    return render(request, 'admin/all-schedules.html')


