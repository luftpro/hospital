from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from accounts.models import Doctor
from .models import Appointment
from django.contrib import messages
import datetime

def index(request):
    if request.method == 'POST' and request.POST.__contains__('name'):
        print(request.POST)
        doctor_iin = request.COOKIES.get('diin')
        print(request.COOKIES.get('diin'))
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = datetime.datetime.strptime(request.POST.get('date'), '%d/%m/%Y').date()
        email = request.POST.get('email')
        print(request.COOKIES.get('tinterval'))
        time_begin = datetime.datetime.strptime(request.COOKIES.get('tinterval').split('-')[0], '%H:%M').time()
        time_end = datetime.datetime.strptime(request.COOKIES.get('tinterval').split('-')[1], '%H:%M').time()
        
       
        Appointment.objects.create(
            name=name,
            phone=phone,
            date=date,
            email=email,
            time_begin=time_begin,  
            time_end=time_end,
            doctor_iin=doctor_iin,
            doc=Doctor.objects.get(iin_number=doctor_iin)
        )
        print('saved')
        messages.success(request, 'Appointment submitted!')
    return render(request, 'index.html')

def therapist(request):
    doctor = Doctor.objects.all()
    return render(request, 'therapist.html', {'doctor' : doctor})

def surgeon(request):
    doctor = Doctor.objects.all()
    return render(request, 'surgeon.html', {'doctor' : doctor})

def physiologist(request):
    doctor = Doctor.objects.all()
    return render(request, 'physiologist.html', {'doctor' : doctor})

def psychologist(request):
    doctor = Doctor.objects.all()
    return render(request, 'psychologist.html', {'doctor' : doctor})
