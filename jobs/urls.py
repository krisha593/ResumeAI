from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.job_recommendations, name='job_recommendations'),
    path('courses/', views.course_recommendations, name='course_recommendations'),
    path('generate/', views.generate_recommendations, name='generate_recommendations'),
]