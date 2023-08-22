from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    USER_TYPES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)



