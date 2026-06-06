from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from analyzer.models import Resume, ResumeAnalysis
from jobs.models import JobRecommendation, CourseRecommendation
from accounts.models import UserProfile


def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    resumes = Resume.objects.filter(user=request.user)
    latest_resume = resumes.filter(status='completed').first()
    latest_analysis = None
    if latest_resume and hasattr(latest_resume, 'analysis'):
        latest_analysis = latest_resume.analysis

    job_count = JobRecommendation.objects.filter(user=request.user).count()
    course_count = CourseRecommendation.objects.filter(user=request.user).count()
    resume_count = resumes.count()

    recent_activity = []
    for r in resumes[:5]:
        recent_activity.append({
            'type': 'resume',
            'icon': 'file-earmark-pdf',
            'color': 'primary',
            'message': f'Uploaded: {r.original_filename}',
            'time': r.uploaded_at,
        })

    context = {
        'profile': profile,
        'latest_analysis': latest_analysis,
        'latest_resume': latest_resume,
        'resume_count': resume_count,
        'job_count': job_count,
        'course_count': course_count,
        'recent_activity': recent_activity,
    }
    return render(request, 'dashboard/dashboard.html', context)


def is_admin(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = User.objects.count()
    total_resumes = Resume.objects.count()
    total_analyses = ResumeAnalysis.objects.count()
    avg_resume_score = ResumeAnalysis.objects.aggregate(avg=Avg('resume_score'))['avg'] or 0
    avg_ats_score = ResumeAnalysis.objects.aggregate(avg=Avg('ats_score'))['avg'] or 0
    
    recent_users = User.objects.order_by('-date_joined')[:10]
    recent_resumes = Resume.objects.order_by('-uploaded_at')[:10]
    
    # Role distribution
    role_data = ResumeAnalysis.objects.values('detected_role').annotate(
        count=Count('id')).order_by('-count')[:6]

    context = {
        'total_users': total_users,
        'total_resumes': total_resumes,
        'total_analyses': total_analyses,
        'avg_resume_score': round(avg_resume_score, 1),
        'avg_ats_score': round(avg_ats_score, 1),
        'recent_users': recent_users,
        'recent_resumes': recent_resumes,
        'role_data': role_data,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)