from django.contrib import admin
from .models import JobRecommendation, CourseRecommendation

@admin.register(JobRecommendation)
class JobAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'company', 'match_percentage', 'created_at']

@admin.register(CourseRecommendation)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'provider', 'skill_covered', 'level', 'rating']