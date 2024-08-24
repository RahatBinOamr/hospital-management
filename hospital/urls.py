from django.urls import path
from .views import appointment_page,doctor_page,single_doctor_page,department_page,single_department_page,load_doctors



urlpatterns =[
  path('appointment',appointment_page, name='appointment'),
  path('ajax/load-doctors/', load_doctors, name='load_doctors'),
  path('doctors',doctor_page, name='doctors'),
  path('doctor/<slug:slug>', single_doctor_page, name='doctor'),
  path('departments', department_page, name='departments'),
  path('department/<slug:slug>', single_department_page,name='department'),

]