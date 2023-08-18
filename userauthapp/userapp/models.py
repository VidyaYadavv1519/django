# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     address_line1 = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     pincode = models.CharField(max_length=10)
#     user_type = models.CharField(max_length=10)  

#     def __str__(self):
#         return self.username

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



