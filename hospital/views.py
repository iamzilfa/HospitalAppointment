from django.shortcuts import render, redirect
from .forms import DepartmentForm, DoctorForm, ScheduleForm, UpdateDepartmentForm, UpdateScheduleForm
from .models import Department, Doctor, Schedule

def index(request):
    return render(request, 'index.html')

# def save_department(request):
#     form = DepartmentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     departments = Department.objects.all()

#     return render(request, 'admin/all-departments.html', context ={'departments': departments})

# def save_doctor(request):
#     if request.method == "POST":
#         form = DoctorForm(request.POST, request.FILES)
#         print(form.errors)
#         if form.is_valid():
#             form.save()
#             return redirect('all_doctors')
#     else:
#         form = DoctorForm()
#         return render(request, "admin/new-doctor.html", context={"form":form})



# def delete_department(request, pk):
#     department = get_object_or_404(Department, pk=pk)
#     department_pk = department.pk
#     department.delete()
#     return redirect("project_detail", pk=project_pk)

def all_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin/all-departments.html', context={"departments": departments})

def new_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-departments')
    else:
        form = DepartmentForm()
        return render(request, 'admin/new-department.html',{'form': form})

def update_department(request,pk):
    dep = Department.objects.get(pk = pk)

    if request.method == "POST":
        form = UpdateDepartmentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Department.objects.filter(id = pk).update(name = name, description = description)

            return redirect("all-departments")
    else:
        form = UpdateDepartmentForm()
    return render(request, "admin/update-department.html", context={"form": form, "department":dep})

def department_delete(request,pk):
    department = Department.objects.get(pk=pk)
    department.delete()

    return redirect('all-departments')


# Doctor View Function

def all_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'admin/all-doctors.html', context={"doctors": doctors})

def new_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
        return render(request, "admin/new-doctor.html", context={"form":form})


def doctor_delete(request,pk):
    doctor = Doctor.objects.get(pk=pk)
    doctor.delete()

    return redirect('doctors')


def all_schedules(request):
    schedules = Schedule.objects.all()
    return render(request, 'admin/all-schedules.html', {"schedules": schedules})

def new_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('schedules')
    else:
        form = ScheduleForm()
        return render(request, 'admin/new-schedule.html', {'form': form})

def update_schedule(request, pk):
    schedule = Schedule.objects.get(pk = pk)
    if request.method == 'POST':
        form = UpdateScheduleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            app_date = form.cleaned_data['app_date']
            app_hour = form.cleaned_data['app_hour']
            Schedule.objects.filter(id = pk).update(app_date = app_date, app_hour = app_hour)
            return redirect('schedules')
    else:
        form = UpdateScheduleForm()
        return render(request, 'admin/update-schedule.html', {'form': form, "schedule": schedule})


def schedule_delete(request,pk):
    schedule = Schedule.objects.get(pk=pk)
    schedule.delete()

    return redirect('schedules')
