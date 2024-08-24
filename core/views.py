from django.shortcuts import redirect, render

from hospital.forms import AppointmentForm

from django.contrib import messages

# Create your views here.
def home_page(request):
  if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment create successfully!!!')
            return redirect(request.path)
  else:
        form = AppointmentForm()
  return render(request, 'index.html', {'form': form})

def about_page(request):
  return render(request, 'about.html')


def service_page(request):
  return render(request, 'services.html')


def contact_page(request):
  return render(request, 'contact.html')