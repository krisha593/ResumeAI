from django.db import models
from django.contrib.auth.models import User


class JobRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_recommendations')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, default='Full-time')
    experience_required = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=100, blank=True)
    required_skills = models.JSONField(default=list)
    match_percentage = models.IntegerField(default=0)
    job_url = models.URLField(blank=True, default='#')
    description = models.TextField(blank=True)
    logo_initial = models.CharField(max_length=3, blank=True)
    color_class = models.CharField(max_length=20, default='primary')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-match_percentage']

    def __str__(self):
        return f"{self.title} at {self.company} ({self.match_percentage}%)"


class CourseRecommendation(models.Model):
    LEVEL_CHOICES = [('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_recommendations')
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    skill_covered = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    duration = models.CharField(max_length=50)
    rating = models.FloatField(default=4.0)
    is_free = models.BooleanField(default=False)
    course_url = models.URLField(blank=True, default='#')
    description = models.TextField(blank=True)
    color_class = models.CharField(max_length=20, default='info')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return f"{self.title} - {self.provider}"