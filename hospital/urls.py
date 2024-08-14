from django.urls import path
from .views import appointment_page
urlpatterns =[
  path('appointment',appointment_page, name='appointment')
]