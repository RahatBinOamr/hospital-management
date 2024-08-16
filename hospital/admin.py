from django.contrib import admin
from .models import Department, Service


class ServiceInline(admin.TabularInline):
  model = Service


class DepartmentAdmin(admin.ModelAdmin):
  inlines = [ServiceInline]


admin.site.register(Department,DepartmentAdmin)
admin.site.register(Service)


