from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    # url('^admin/',views.admin, name = 'main-dashboard'),
    url('^admin/departments',views.all_departments, name = 'departments'),
    url('^admin/new-department',views.new_department, name = 'new_department'),
    url('^admin/doctors',views.all_doctors, name = 'doctors'),
    url('^admin/new-doctor',views.new_doctor, name = 'new_doctor'),
    url('^admin/schedules',views.all_schedules, name = 'schedules'),
    url('^admin/new-schedule',views.new_schedule, name = 'new_schedule'),
]    