from django.urls import path
from .views import (
    appointment_page,
    doctor_page,
    single_doctor_page,
    department_page,
    single_department_page,
    load_doctors,
    gynecology_doctor_page,
    pulmology_doctor_page,
    child_care_doctor_page,
    dental_doctor_page,
    cardiology_doctor_page,
    opthomology_doctor_page,
    confirmation_page,
)

urlpatterns = [
    path('appointment/', appointment_page, name='appointment'),
    path('confirmation/', confirmation_page, name='confirmation'),
    path('ajax/load-doctors/', load_doctors, name='load_doctors'),
    path('doctors/', doctor_page, name='doctors'),
    path('doctor/<slug:slug>/', single_doctor_page, name='doctor'),
    path('departments/', department_page, name='departments'),
    path('department/<slug:slug>/', single_department_page, name='department'),
    path('gynecology/', gynecology_doctor_page, name='gynecology_doctors'),
    path('pulmology/', pulmology_doctor_page, name='pulmology_doctors'),
    path('child-care/', child_care_doctor_page, name='child_care_doctors'),
    path('dental/', dental_doctor_page, name='dental_doctors'),
    path('cardiology/', cardiology_doctor_page, name='cardiology_doctors'),
    path('opthomology/', opthomology_doctor_page, name='opthomology_doctors'),
]
