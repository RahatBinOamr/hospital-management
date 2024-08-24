from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from hospital.forms import AppointmentForm
from .models import Department,Doctor, EducationalQualification, Expertise
from django.contrib import messages
# Create your views here.
def appointment_page(request):
  if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment create successfully!!!')
            return redirect('confirmation')
  else:
        form = AppointmentForm()
  return render(request, 'appointment.html',{'form':form})


def confirmation_page(request):
    return render(request, 'confirmation.html')

def load_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Doctor.objects.filter(department_id=department_id).order_by('name')
    return JsonResponse(list(doctors.values('id', 'name')), safe=False)

def doctor_page(request):
  doctors = Doctor.objects.all()
  context = {'doctors': doctors}
  return render(request, 'doctor.html',context)

def gynecology_doctor_page(request):
    department = get_object_or_404(Department, name='Gynecology')
    doctors = Doctor.objects.filter(department=department)
    context = {'doctors': doctors}
    return render(request, 'gynecology.html', context)

def pulmology_doctor_page(request):
    department = get_object_or_404(Department, name='Pulmology')
    doctors = Doctor.objects.filter(department=department)
    context = {'doctors': doctors}
    return render(request, 'pulmology.html', context)

def child_care_doctor_page(request):
    department = get_object_or_404(Department, name='Child Care')
    doctors = Doctor.objects.filter(department=department)
    context = {'doctors': doctors}
    return render(request, 'child_care.html', context)

def dental_doctor_page(request):
    department = get_object_or_404(Department, name='Dental Care')
    doctors = Doctor.objects.filter(department=department)
    context = {'doctors': doctors}
    return render(request, 'dental.html', context)

def cardiology_doctor_page(request):
    department = get_object_or_404(Department, name='Cardiology')
    doctors = Doctor.objects.filter(department=department)
    context = {'doctors': doctors}
    return render(request, 'cardiology.html', context)

def opthomology_doctor_page(request):
    department = get_object_or_404(Department, name='Opthomology')
    doctors = Doctor.objects.filter(department=department)
    context = {'doctors': doctors}
    return render(request, 'opthomology.html', context)






def single_doctor_page(request, slug):
    doctor = Doctor.objects.get(slug=slug)
    qualifications = EducationalQualification.objects.filter(doctor=doctor)
    expertise_areas = Expertise.objects.filter(doctor=doctor)
    
    context = {
        'doctor': doctor,
        'qualifications': qualifications,
        'expertise_areas': expertise_areas,
    }
    return render(request, 'single_doctor.html', context)


def department_page(request):
  department = Department.objects.all()
  context ={
    'department': department
  }
  return render(request, 'department.html',context)

def single_department_page(request, slug):
    department = Department.objects.get(d_slug=slug)
    services = department.service_set.all()  
    context = {
        'item': department,
        'services': services  
    }
    return render(request, 'single_department.html', context)