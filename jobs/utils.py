"""Generate AI-based job and course recommendations based on resume analysis."""

JOB_DATABASE = [
    {'title': 'Python Developer', 'company': 'TechCorp Solutions', 'location': 'Bangalore, India',
     'type': 'Full-time', 'exp': '0-2 years', 'salary': '₹4-7 LPA',
     'skills': ['python', 'django', 'flask', 'sql', 'git'], 'color': 'primary', 'logo': 'TC'},
    {'title': 'React Frontend Developer', 'company': 'WebMinds Pvt Ltd', 'location': 'Mumbai, India',
     'type': 'Full-time', 'exp': '1-3 years', 'salary': '₹5-9 LPA',
     'skills': ['react', 'javascript', 'html', 'css', 'node.js'], 'color': 'info', 'logo': 'WM'},
    {'title': 'Data Scientist', 'company': 'Analytics Hub', 'location': 'Hyderabad, India',
     'type': 'Full-time', 'exp': '1-3 years', 'salary': '₹6-12 LPA',
     'skills': ['python', 'machine learning', 'pandas', 'numpy', 'sql'], 'color': 'success', 'logo': 'AH'},
    {'title': 'Full Stack Developer', 'company': 'StartupLaunch', 'location': 'Pune, India',
     'type': 'Full-time', 'exp': '2-4 years', 'salary': '₹7-14 LPA',
     'skills': ['python', 'django', 'react', 'javascript', 'postgresql', 'docker'], 'color': 'warning', 'logo': 'SL'},
    {'title': 'DevOps Engineer', 'company': 'CloudFirst Tech', 'location': 'Delhi, India',
     'type': 'Full-time', 'exp': '2-5 years', 'salary': '₹8-15 LPA',
     'skills': ['docker', 'kubernetes', 'aws', 'jenkins', 'linux', 'git'], 'color': 'danger', 'logo': 'CF'},
    {'title': 'ML Engineer', 'company': 'AI Ventures', 'location': 'Bangalore, India',
     'type': 'Full-time', 'exp': '1-3 years', 'salary': '₹8-16 LPA',
     'skills': ['python', 'tensorflow', 'pytorch', 'deep learning', 'docker'], 'color': 'purple', 'logo': 'AV'},
    {'title': 'Backend Developer', 'company': 'FinTech Solutions', 'location': 'Chennai, India',
     'type': 'Full-time', 'exp': '1-3 years', 'salary': '₹5-10 LPA',
     'skills': ['python', 'django', 'postgresql', 'redis', 'aws'], 'color': 'secondary', 'logo': 'FS'},
    {'title': 'Data Analyst', 'company': 'Insight Analytics', 'location': 'Kolkata, India',
     'type': 'Full-time', 'exp': '0-2 years', 'salary': '₹3-6 LPA',
     'skills': ['sql', 'python', 'excel', 'tableau', 'power bi'], 'color': 'teal', 'logo': 'IA'},
    {'title': 'Software Engineer Intern', 'company': 'Google India', 'location': 'Bangalore, India',
     'type': 'Internship', 'exp': 'Fresher', 'salary': '₹50K/month',
     'skills': ['python', 'java', 'c++', 'algorithms', 'git'], 'color': 'success', 'logo': 'G'},
    {'title': 'Cloud Solutions Architect', 'company': 'Amazon AWS', 'location': 'Hyderabad, India',
     'type': 'Full-time', 'exp': '3-7 years', 'salary': '₹20-40 LPA',
     'skills': ['aws', 'terraform', 'kubernetes', 'python', 'linux'], 'color': 'warning', 'logo': 'AM'},
]

COURSE_DATABASE = [
    {'title': 'Complete Python Bootcamp', 'provider': 'Udemy', 'skill': 'python',
     'level': 'Beginner', 'duration': '22 hours', 'rating': 4.6, 'free': False,
     'url': 'https://udemy.com', 'color': 'primary',
     'desc': 'Learn Python from scratch with projects and exercises.'},
    {'title': 'Machine Learning A-Z', 'provider': 'Udemy', 'skill': 'machine learning',
     'level': 'Intermediate', 'duration': '44 hours', 'rating': 4.5, 'free': False,
     'url': 'https://udemy.com', 'color': 'success',
     'desc': 'Hands-on machine learning with Python and R.'},
    {'title': 'React - The Complete Guide', 'provider': 'Udemy', 'skill': 'react',
     'level': 'Intermediate', 'duration': '49 hours', 'rating': 4.7, 'free': False,
     'url': 'https://udemy.com', 'color': 'info',
     'desc': 'Build powerful React applications from scratch.'},
    {'title': 'AWS Cloud Practitioner', 'provider': 'AWS Training', 'skill': 'aws',
     'level': 'Beginner', 'duration': '6 hours', 'rating': 4.8, 'free': True,
     'url': 'https://aws.amazon.com/training', 'color': 'warning',
     'desc': 'Official AWS cloud fundamentals course.'},
    {'title': 'Docker & Kubernetes Masterclass', 'provider': 'Udemy', 'skill': 'docker',
     'level': 'Intermediate', 'duration': '18 hours', 'rating': 4.6, 'free': False,
     'url': 'https://udemy.com', 'color': 'danger',
     'desc': 'Master containerization and orchestration.'},
    {'title': 'Django REST Framework', 'provider': 'TestDriven.io', 'skill': 'django',
     'level': 'Intermediate', 'duration': '12 hours', 'rating': 4.7, 'free': False,
     'url': 'https://testdriven.io', 'color': 'secondary',
     'desc': 'Build production-ready REST APIs with Django.'},
    {'title': 'Data Analysis with Python', 'provider': 'Coursera', 'skill': 'pandas',
     'level': 'Beginner', 'duration': '25 hours', 'rating': 4.5, 'free': True,
     'url': 'https://coursera.org', 'color': 'teal',
     'desc': 'Learn data manipulation with Pandas and NumPy.'},
    {'title': 'Deep Learning Specialization', 'provider': 'Coursera', 'skill': 'deep learning',
     'level': 'Advanced', 'duration': '80 hours', 'rating': 4.9, 'free': False,
     'url': 'https://coursera.org', 'color': 'purple',
     'desc': 'Andrew Ng\'s deep learning specialization.'},
    {'title': 'JavaScript Algorithms', 'provider': 'freeCodeCamp', 'skill': 'javascript',
     'level': 'Intermediate', 'duration': '40 hours', 'rating': 4.4, 'free': True,
     'url': 'https://freecodecamp.org', 'color': 'warning',
     'desc': 'Master JavaScript and data structures.'},
    {'title': 'SQL for Data Science', 'provider': 'Coursera', 'skill': 'sql',
     'level': 'Beginner', 'duration': '16 hours', 'rating': 4.3, 'free': True,
     'url': 'https://coursera.org', 'color': 'info',
     'desc': 'Learn SQL for data analysis and science.'},
]


def calculate_match(job_skills, user_skills):
    """Calculate job match percentage."""
    if not job_skills:
        return 0
    user_lower = [s.lower() for s in user_skills]
    matched = sum(1 for s in job_skills if s.lower() in user_lower)
    return int((matched / len(job_skills)) * 100)


def generate_job_recommendations(user, analysis):
    """Generate and save job recommendations."""
    from .models import JobRecommendation
    
    JobRecommendation.objects.filter(user=user).delete()
    user_skills = analysis.extracted_skills or []
    
    recommendations = []
    for job in JOB_DATABASE:
        match = calculate_match(job['skills'], user_skills)
        if match >= 20:
            recommendations.append({
                'job': job,
                'match': match,
            })
    
    recommendations.sort(key=lambda x: x['match'], reverse=True)
    
    saved = []
    for item in recommendations[:8]:
        job = item['job']
        jr = JobRecommendation.objects.create(
            user=user,
            title=job['title'],
            company=job['company'],
            location=job['location'],
            job_type=job['type'],
            experience_required=job['exp'],
            salary_range=job['salary'],
            required_skills=job['skills'],
            match_percentage=item['match'],
            logo_initial=job['logo'],
            color_class=job['color'],
        )
        saved.append(jr)
    return saved


def generate_course_recommendations(user, analysis):
    """Generate and save course recommendations."""
    from .models import CourseRecommendation
    
    CourseRecommendation.objects.filter(user=user).delete()
    missing_skills = analysis.missing_skills or []
    user_skills = analysis.extracted_skills or []
    
    # Prioritize missing skills, then expand with relevant courses
    priority_skills = missing_skills[:5]
    
    saved = []
    for course in COURSE_DATABASE:
        skill = course['skill'].lower()
        is_missing = any(skill in ms.lower() or ms.lower() in skill for ms in priority_skills)
        is_relevant = any(skill in us.lower() or us.lower() in skill for us in user_skills)
        
        if is_missing or is_relevant or len(saved) < 4:
            cr = CourseRecommendation.objects.create(
                user=user,
                title=course['title'],
                provider=course['provider'],
                skill_covered=course['skill'],
                level=course['level'],
                duration=course['duration'],
                rating=course['rating'],
                is_free=course['free'],
                course_url=course['url'],
                description=course['desc'],
                color_class=course['color'],
            )
            saved.append(cr)
        
        if len(saved) >= 8:
            break
    
    return saved