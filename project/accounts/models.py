from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class Degree(models.TextChoices):
    MD = 'MD', 'MD'
    PHD = 'PH', 'PhD'

class Blood(models.TextChoices):
    OPOS = 'OP', 'O(+)'
    ONEG = 'ON', 'O(-)'
    APOS = 'AP', 'A(+)'
    ANEG = 'AN', 'A(-)'
    BPOS = 'BP', 'B(+)'
    BNEG = 'BN', 'B(-)'
    ABPOS = 'ABP', 'AB(+)'
    ABNEG = 'ABN', 'AB(-)'

class Marital(models.TextChoices):
    SINGLE = 'SIN', 'Single'
    MARRIED = 'MAR', 'Married'
    DIVORCED = 'DIV', 'Divorced'
    OTHER = 'OTH', 'Other'

class Gender(models.TextChoices):
    FEMALE = 'F', 'Female'
    MALE = 'M', 'Male'


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    first_name = None
    last_name = None


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    iin_number = models.CharField(
        max_length=12, 
        validators=[RegexValidator(r'^\d{12,12}$')],
        unique=True,
        verbose_name='IIN'
    )
    id_number = models.CharField(
        max_length=9,
        validators=[RegexValidator(r'^\d{9,9}$')], 
        unique=True,
        verbose_name='State ID number'
    )
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )
    blood_group = models.CharField(
        max_length=3,
        choices=Blood.choices
    )
    contact_number = models.CharField(max_length=15, validators = [RegexValidator(r'^\+?1?\d{9,15}$')])
    emergency_contact = models.CharField(
        max_length=15, 
        validators = [RegexValidator(r'^\+?1?\d{9,15}$')]
    )
    address = models.CharField(max_length=200, blank=True)
    marital_status = models.CharField(
        max_length=3,
        choices=Marital.choices,
        default=Marital.OTHER
    )

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    iin_number = models.CharField(
        max_length=12, 
        validators=[RegexValidator(r'^\d{12,12}$')],
        unique=True,
        verbose_name='IIN'
    )
    id_number = models.CharField(
        max_length=9, 
        validators=[RegexValidator(r'^\d{9,9}$')], 
        unique=True,
        verbose_name='State ID number'
    )
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )
    blood_group = models.CharField(
        max_length=3,
        choices=Blood.choices
    )
    contact_number = models.CharField(max_length=15, validators = [RegexValidator(r'^\+?1?\d{9,15}$')])
    department_id = models.IntegerField(verbose_name='Department ID')
    special_id = models.IntegerField(verbose_name='Special ID')
    experience = models.IntegerField(verbose_name='Years of experience')
    photo = models.ImageField(blank=True)
    category = models.CharField(max_length=150)
    price = models.IntegerField(verbose_name='Appointment price')
    schedule_details = models.TextField(blank=True, default='')
    degree = models.CharField(
        max_length=2,
        choices=Degree.choices
    )
    rating = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        blank=True,
        null=True
    )
    address = models.CharField(max_length=200, blank=True)
    homepage = models.URLField(max_length=254, blank=True)