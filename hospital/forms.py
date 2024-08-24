from django import forms
from .models import Appointment, Doctor

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['department', 'doctor', 'date', 'time', 'full_name', 'phone_number', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM', 'type': 'time'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['doctor'].queryset = Doctor.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.department.doctor_set.order_by('name')
