from django.db import models
from accounts.models import Doctor
from django.core.validators import RegexValidator

class Appointment(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField()
    time_begin = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Begin time')
    time_end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Finish time')
    doctor_iin = models.CharField(max_length=12, verbose_name='Doctor IIN')
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)