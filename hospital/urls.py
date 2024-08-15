from django.urls import path
from .views import appointment_page,doctor_page,single_doctor_page,department_page,single_department_page



urlpatterns =[
  path('appointment',appointment_page, name='appointment'),
  path('doctors',doctor_page, name='doctors'),
  path('doctor', single_doctor_page, name='doctor'),
  path('departments', department_page, name='departments'),
  path('department', single_department_page,name='department'),

]