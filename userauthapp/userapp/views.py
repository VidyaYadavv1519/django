from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserSignupForm, UserLoginForm, BlogPostForm
from .models import User,Category,BlogPost
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


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



@login_required  
def dashboard(request):
    user = request.user  
    return render(request, 'dashboard.html', {'user': user})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
         
            blog_post.save()
            return redirect('userapp:dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def patient_dashboard(request):
    categories = Category.objects.all()
    posts_by_category = {}
    for category in categories:
        posts = BlogPost.objects.filter(category=category, draft=False)
        posts_by_category[category] = posts
    return render(request, 'patient_dashboard.html', {'posts_by_category': posts_by_category})



