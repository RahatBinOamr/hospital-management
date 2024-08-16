from django.shortcuts import render
from .models import Department
# Create your views here.
def appointment_page(request):
  return render(request, 'appointment.html')

def doctor_page(request):
  return render(request, 'doctor.html')


def single_doctor_page(request):
  return render(request, 'single_doctor.html')


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