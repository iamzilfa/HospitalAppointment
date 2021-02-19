from django.shortcuts import render
from .forms import DepartmentForm

def index(request):
    return render(request, 'index.html')

def new_department(request):
    departform = DepartmentForm()
    return render(request, 'admin/new-department.html', {'form': departform})

def all_departments(request):
    return render(request, 'admin/all-departments.html')

# def admin(request):
#     return render(request, 'admin/main.html')

# def add_department(request):
#     departform = DepartmentForm()
#     return render(request, 'admin/new-department.html', {'form': departform})

