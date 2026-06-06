content = """from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume, ResumeAnalysis
from .utils import analyze_resume


@login_required
def upload_resume(request):
    if request.method == 'POST':
        if 'resume_file' not in request.FILES:
            messages.error(request, 'Please select a file.')
            return redirect('upload_resume')
        file = request.FILES['resume_file']
        if not file.name.lower().endswith('.pdf'):
            messages.error(request, 'Only PDF files are supported.')
            return redirect('upload_resume')
        if file.size > 5 * 1024 * 1024:
            messages.error(request, 'File size must be under 5MB.')
            return redirect('upload_resume')
        Resume.objects.filter(user=request.user).update(is_active=False)
        resume = Resume.objects.create(
            user=request.user,
            file=file,
            original_filename=file.name,
            status='analyzing'
        )
        try:
            analyze_resume(resume)
            messages.success(request, 'Resume analyzed successfully!')
            return redirect('resume_analysis', pk=resume.pk)
        except Exception as e:
            messages.error(request, 'Analysis failed. Please try again.')
            return redirect('upload_resume')
    recent_resumes = Resume.objects.filter(user=request.user)[:5]
    return render(request, 'analyzer/upload.html', {'recent_resumes': recent_resumes})


@login_required
def resume_analysis(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    analysis = get_object_or_404(ResumeAnalysis, resume=resume)
    return render(request, 'analyzer/analysis.html', {
        'resume': resume,
        'analysis': analysis
    })


@login_required
def analysis_list(request):
    resumes = Resume.objects.filter(user=request.user).select_related('analysis')
    return render(request, 'analyzer/list.html', {'resumes': resumes})
"""

with open('analyzer/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS - analyzer/views.py fixed!")
print("Functions:", [line.strip() for line in content.split('\n') if line.startswith('def ')])