from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    # path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    # path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]