from django.db import models
from django.contrib.auth.models import User

JOB_STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]

APPLICATION_STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('interviewing', 'Interviewing'),
    ('hired', 'Hired'),
    ('rejected', 'Rejected'),
]

class JobPosting(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=16, choices=JOB_STATUS_CHOICES, default='open')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True) # Ensures one profile per email
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=16, choices=APPLICATION_STATUS_CHOICES, default='applied')
    notes = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job')

    def __str__(self):
        return f"{self.job} Application - {self.applicant}"