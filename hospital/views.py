from django.shortcuts import render
from .forms import DepartmentForm, DoctorForm, ScheduleForm
from .models import Department, Doctor

def index(request):
    return render(request, 'index.html')

def save_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
    # context= {'form': form }
    departments = Department.objects.all()

    return render(request, 'admin/all-departments.html', context ={'departments': departments})

def save_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            doctors = Doctor.objects.all()
            return render(request, 'admin/all-doctors.html', context ={'doctors': doctors})
    else:
        form = DoctorForm()
    return render(request, "admin/new-doctor.html", context={"form":form})

def update_department(request,pk):
    if request.method == "POST":
        form = UpdateDepartmentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("all-departments")
    else:
        form = UpdateDepartmentForm()
    return render(request, 'admin/update-department.html', context={"form":form})

def doctor_delete(request,pk):
    doctor = Doctor.objects.get(pk=pk)
    doctor.delete()

    return redirect('all_doctors')

def department_delete(request,pk):
    department = Department.objects.get(pk=pk)
    department.delete()

    return render(request, 'admin/all-departments.html')

# def delete_department(request, pk):
#     department = get_object_or_404(Department, pk=pk)
#     department_pk = department.pk
#     department.delete()
#     return redirect("project_detail", pk=project_pk)

def all_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin/all-departments.html', context={"departments": departments})

def new_department(request):
    departform = DepartmentForm()
    return render(request, 'admin/new-department.html',{'form': departform})

def new_doctor(request):
    doctorform = DoctorForm()
    return render(request, 'admin/new-doctor.html', {'form': doctorform})

def all_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'admin/all-doctors.html', context={"doctors": doctors})

def new_schedule(request):
    return render(request, 'admin/new-schedule.html', {'form': scheduleform})

def all_schedules(request):
    return render(request, 'admin/all-schedules.html')


# class new_department( CreateView):
#     redirect_field_name = "admin/all_departments.html"
#     model = Department
#     form_class = DepartmentForm
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["current_user"] = self.request.user
#         return context
