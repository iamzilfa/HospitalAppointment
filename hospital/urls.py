from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    # url('^admin/',views.admin, name = 'main-dashboard'),
    url('^admin/departments',views.all_departments, name = 'departments'),
    url('^admin/all-departments',views.all_departments, name = 'all-departments'),
    url('^admin/new-department',views.new_department, name = 'new_department'),
    url('^admin/save-department',views.save_department, name = 'save_department'),
    url('^admin/doctors',views.all_doctors, name = 'doctors'),
    url('^admin/new-doctor',views.new_doctor, name = 'new_doctor'),
    url('^admin/save-doctor',views.save_doctor, name = 'save_doctor'),
    url('^admin/schedules',views.all_schedules, name = 'schedules'),
    url('^admin/new-schedule',views.new_schedule, name = 'new_schedule'),
    url('^admin/department_delete/(?P<pk>\d+)$',views.department_delete, name = 'department_delete'),
    url('^admin/doctor_delete/(?P<pk>\d+)$',views.doctor_delete, name = 'doctor_delete'),
    url('^admin/update_department/(?P<pk>\d+)$',views.update_department, name = 'update_department'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
