from django.contrib import admin
from accounts.models import User, Patient, Doctor
from appointment.models import Appointment
from django.contrib.auth.hashers import make_password

admin.site.site_header = 'Hospital Management'
admin.site.index_title = 'Hospital Management System'
admin.site.site_title = 'Hospital Management'

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = (
        'name',
        'phone',
        'date',
        'email',
        'time_begin',
        'time_end',
        'doc_name',
        'doc_lastname',
        'doctor_iin'
    )
    def doc_name(self, obj):
        return obj.doc.first_name
    def doc_lastname(self, obj):
        return obj.doc.last_name

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_patient', 'is_doctor', 'is_staff', 'is_active')
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        obj.user = request.user
        obj.save()

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = (
        'username', 
        'first_name', 
        'last_name', 
        'iin_number',
        'id_number',
        'date_of_birth', 
        'gender', 
        'blood_group',
        'contact_number',
        'emergency_contact',
        'address',
        'marital_status'
    )
    search_fields = ( 
        'first_name', 
        'last_name', 
        'iin_number',
        'id_number',
        'date_of_birth', 
        'gender', 
        'blood_group',
        'contact_number',
        'emergency_contact',
        'address',
        'marital_status'
    )

    def username(self, obj):
        return obj.user.username

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = (
        'username', 
        'first_name', 
        'last_name', 
        'iin_number',
        'id_number',
        'date_of_birth', 
        'gender', 
        'blood_group', 
        'department_id',
        'special_id',
        'experience',
        'category',
        'price',
        'degree',
        'rating',
        'contact_number',
        'schedule_details',
        'address',
        'homepage'
    )
    search_fields = ( 
        'first_name', 
        'last_name', 
        'iin_number',
        'id_number',
        'date_of_birth', 
        'gender', 
        'blood_group', 
        'department_id',
        'special_id',
        'experience',
        'category',
        'price',
        'degree',
        'rating',
        'contact_number',
        'schedule_details',
        'address',
        'homepage'
    )

    def username(self, obj):
        return obj.user.username

admin.site.register(User, UserAdmin)
admin.site.register(Appointment, AppointmentAdmin)