from django.shortcuts import redirect, render

from hospital.forms import AppointmentForm

from django.contrib import messages

from hospital.models import Doctor

# Create your views here.
def home_page(request):
  if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment create successfully!!!')
            return redirect('confirmation')
  else:
        form = AppointmentForm()
  return render(request, 'index.html', {'form': form})

def about_page(request):
  doctors = Doctor.objects.all().order_by('?')[:4]
  context = {'doctors': doctors}
  return render(request, 'about.html',context)


def service_page(request):
  return render(request, 'services.html')


def contact_page(request):
  return render(request, 'contact.html')