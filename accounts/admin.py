from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'location', 'desired_role', 'experience_years', 'created_at']
    search_fields = ['user__username', 'user__email', 'location', 'desired_role']