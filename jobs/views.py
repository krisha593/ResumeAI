from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobRecommendation, CourseRecommendation
from .utils import generate_job_recommendations, generate_course_recommendations
from analyzer.models import ResumeAnalysis, Resume


@login_required
def job_recommendations(request):
    jobs = JobRecommendation.objects.filter(user=request.user)
    
    if not jobs.exists():
        # Try to generate from latest analysis
        try:
            latest_resume = Resume.objects.filter(user=request.user, status='completed').first()
            if latest_resume and hasattr(latest_resume, 'analysis'):
                generate_job_recommendations(request.user, latest_resume.analysis)
                jobs = JobRecommendation.objects.filter(user=request.user)
        except Exception:
            pass
    
    return render(request, 'jobs/jobs.html', {'jobs': jobs})


@login_required
def course_recommendations(request):
    courses = CourseRecommendation.objects.filter(user=request.user)
    
    if not courses.exists():
        try:
            latest_resume = Resume.objects.filter(user=request.user, status='completed').first()
            if latest_resume and hasattr(latest_resume, 'analysis'):
                generate_course_recommendations(request.user, latest_resume.analysis)
                courses = CourseRecommendation.objects.filter(user=request.user)
        except Exception:
            pass
    
    return render(request, 'jobs/courses.html', {'courses': courses})


@login_required
def generate_recommendations(request):
    try:
        latest_resume = Resume.objects.filter(user=request.user, status='completed').first()
        if latest_resume and hasattr(latest_resume, 'analysis'):
            generate_job_recommendations(request.user, latest_resume.analysis)
            generate_course_recommendations(request.user, latest_resume.analysis)
            messages.success(request, '🎯 Recommendations generated based on your resume!')
        else:
            messages.warning(request, 'Please upload and analyze a resume first.')
    except Exception as e:
        messages.error(request, f'Error generating recommendations: {str(e)}')
    return redirect('job_recommendations')