from django.contrib import admin
from .models import User, Category,  BlogPost

# Register your models here.
admin.site.register(User)
admin.site.register(Category)

 
admin.site.register(BlogPost)
