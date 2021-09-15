from django.urls import path
from .views import *
from . import views

app_name='TWILIO'

urlpatterns = [
    path('', Home, name='Home'),
    path('auth_view', auth_view, name='auth_view'),
    path('veryfy_view', veryfy_view, name='veryfy_view'),
]