from django.urls import path
from .views import *

urlpatterns = [
    path('submit/', submit_report, name='submit_report'),
    path('form/', report_form, name='report_form'),
    
]