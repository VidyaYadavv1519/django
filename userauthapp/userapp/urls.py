from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('category_list/', views.category_list, name='category_list'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    
]