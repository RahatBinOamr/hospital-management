from django.shortcuts import render

# Create your views here.
def appointment_page(request):
  return render(request, 'appointment.html')

def doctor_page(request):
  return render(request, 'doctor.html')


def single_doctor_page(request):
  return render(request, 'single_doctor.html')


def department_page(request):
  return render(request, 'department.html')

def single_department_page(request):
  return render(request, 'single_department.html')