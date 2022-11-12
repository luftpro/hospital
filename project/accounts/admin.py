from django.contrib import admin
from accounts.models import User, Patient, Doctor
from django.contrib.auth.hashers import make_password

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_patient', 'is_doctor', 'is_staff', 'is_active')
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        obj.user = request.user
        obj.save()

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ('username', 'first_name', 'last_name', 'iin_number', 'gender', 'blood_group')

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
    search_fields = ('user__username', 'first_name', 'last_name')

    def username(self, obj):
        return obj.user.username

admin.site.register(User, UserAdmin)
