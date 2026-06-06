from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path('analysis/<int:pk>/', views.resume_analysis, name='resume_analysis'),
    path('history/', views.analysis_list, name='analysis_list'),
]