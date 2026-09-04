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
    
# 2. Recruitment Phase Models

class InternshipRole(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.department})"

class Application(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('INTERVIEWING', 'Interviewing'),
        ('HIRED', 'Hired'),
        ('REJECTED', 'Rejected'),
    )

    applicant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'APPLICANT'})
    role = models.ForeignKey(InternshipRole, on_delete=models.CASCADE)
    resume_url = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.role.title} [{self.status}]"