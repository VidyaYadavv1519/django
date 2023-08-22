
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, BlogPost
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'user_type']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']
