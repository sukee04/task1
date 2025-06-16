from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPES = (
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.username
