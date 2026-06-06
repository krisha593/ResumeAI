from django.contrib import admin
from .models import Resume, ResumeAnalysis

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'original_filename', 'status', 'uploaded_at']

@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = ['resume', 'resume_score', 'ats_score', 'detected_role', 'analyzed_at']