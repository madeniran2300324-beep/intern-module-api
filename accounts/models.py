from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # These are the 4 roles from our project specifications
    ROLE_CHOICES = (
        ('APPLICANT', 'Applicant'),
        ('INTERN', 'Intern'),
        ('MENTOR', 'Mentor'),
        ('HR', 'HR Admin'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='APPLICANT')

    def __str__(self):
        return f"{self.username} - {self.role}"