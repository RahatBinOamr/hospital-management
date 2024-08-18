from django.contrib import admin
from .models import Department, Service,Doctor,EducationalQualification,Expertise,DoctorSchedule,Appointment


class ServiceInline(admin.TabularInline):
  model = Service


class DepartmentAdmin(admin.ModelAdmin):
  inlines = [ServiceInline]


class EducationalQualificationInline(admin.TabularInline):
  model = EducationalQualification


class ExpertiseInline(admin.TabularInline):
  model = Expertise

class DoctorScheduleInline(admin.TabularInline):
  model = DoctorSchedule


class DoctorAdmin(admin.ModelAdmin):
  inlines = [EducationalQualificationInline, ExpertiseInline, DoctorScheduleInline]



admin.site.register(Doctor,DoctorAdmin)
admin.site.register(EducationalQualification)
admin.site.register(DoctorSchedule)
admin.site.register(Expertise)

admin.site.register(Appointment)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Service)


