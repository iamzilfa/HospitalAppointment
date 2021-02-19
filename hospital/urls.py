from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    # url('^admin/',views.admin, name = 'main-dashboard'),
    url('^admin/departments',views.all_departments, name = 'departments'),
    url('^admin/new-department',views.new_department, name = 'new_department')
]    