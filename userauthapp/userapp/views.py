from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserSignupForm, UserLoginForm
from .models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('userapp:login')  # Redirect to the login page
#     else:
#         form = UserSignupForm()
#     return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('userapp:login')  # Redirect to the login page
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})








# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             if user.user_type == 'Patient':
#                 return redirect('patient_dashboard')
#             elif user.user_type == 'Doctor':
#                 return redirect('doctor_dashboard')
#     else:
#         form = UserSignupForm()
#     return render(request, 'signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 if user.user_type == 'Patient':
#                     return redirect('patient_dashboard')
#                 elif user.user_type == 'Doctor':
#                     return redirect('doctor_dashboard')
#     else:
#         form = UserLoginForm()
#     return render(request, 'login.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userapp:dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



@login_required  # Requires the user to be logged in
def dashboard(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'dashboard.html', {'user': user})

# def patient_dashboard(request):
#     return render(request, 'patient_dashboard.html', {'user': request.user})

# def doctor_dashboard(request):
#     return render(request, 'doctor_dashboard.html', {'user': request.user})


