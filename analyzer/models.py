from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('analyzing', 'Analyzing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    original_filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.user.username} - {self.original_filename}"


class ResumeAnalysis(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='analysis')
    resume_score = models.IntegerField(default=0)
    ats_score = models.IntegerField(default=0)
    extracted_skills = models.JSONField(default=list)
    missing_skills = models.JSONField(default=list)
    improvement_suggestions = models.JSONField(default=list)
    education_score = models.IntegerField(default=0)
    experience_score = models.IntegerField(default=0)
    skills_score = models.IntegerField(default=0)
    formatting_score = models.IntegerField(default=0)
    keyword_density = models.FloatField(default=0.0)
    detected_role = models.CharField(max_length=100, blank=True)
    experience_level = models.CharField(max_length=50, blank=True)
    raw_text = models.TextField(blank=True)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.resume}"