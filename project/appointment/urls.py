from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, therapist, surgeon, physiologist, psychologist

urlpatterns = [
    path('index/', index, name='Make appointment'),
    path('index/therapist/', therapist, name='Therapists'),
    path('index/surgeon/', surgeon, name='Surgeons'),
    path('index/physiologist/', physiologist, name='Physiologists'),
    path('index/psychologist/', psychologist, name='Psychologists'),
]
