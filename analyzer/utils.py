"""
Resume Analysis Engine - Core AI Logic
Uses keyword extraction and scoring algorithms
"""
import re
import random

# ─── Skill Categories ────────────────────────────────────────────────────────
SKILL_CATEGORIES = {
    'programming': ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift',
                    'kotlin', 'go', 'rust', 'typescript', 'scala', 'r', 'matlab', 'perl'],
    'web': ['html', 'css', 'react', 'angular', 'vue', 'node.js', 'django', 'flask',
            'fastapi', 'spring', 'laravel', 'express', 'jquery', 'bootstrap', 'tailwind', 'next.js'],
    'data': ['machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn',
             'pandas', 'numpy', 'matplotlib', 'seaborn', 'tableau', 'power bi', 'sql',
             'data analysis', 'statistics', 'nlp', 'computer vision', 'spark', 'hadoop'],
    'cloud': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'jenkins',
              'ci/cd', 'devops', 'ansible', 'git', 'github', 'linux', 'nginx'],
    'database': ['mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle', 'firebase',
                 'elasticsearch', 'cassandra', 'dynamodb'],
    'soft': ['leadership', 'communication', 'teamwork', 'problem solving', 'project management',
             'agile', 'scrum', 'time management', 'critical thinking', 'collaboration'],
}

ROLE_SKILL_MAP = {
    'Software Engineer': ['python', 'java', 'c++', 'javascript', 'git', 'agile', 'sql', 'linux'],
    'Data Scientist': ['python', 'machine learning', 'deep learning', 'tensorflow', 'pandas',
                       'numpy', 'statistics', 'sql', 'tableau'],
    'Web Developer': ['html', 'css', 'javascript', 'react', 'node.js', 'git', 'sql', 'bootstrap'],
    'DevOps Engineer': ['docker', 'kubernetes', 'aws', 'jenkins', 'git', 'linux', 'terraform', 'ci/cd'],
    'Data Analyst': ['sql', 'python', 'excel', 'tableau', 'power bi', 'statistics', 'pandas'],
    'ML Engineer': ['python', 'machine learning', 'deep learning', 'tensorflow', 'pytorch',
                    'docker', 'aws', 'git'],
    'Full Stack Developer': ['html', 'css', 'javascript', 'react', 'node.js', 'python',
                             'django', 'sql', 'git', 'docker'],
    'Android Developer': ['java', 'kotlin', 'android', 'firebase', 'git', 'sql'],
    'Cloud Engineer': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'linux'],
}

ATS_KEYWORDS = [
    'experience', 'education', 'skills', 'objective', 'summary', 'projects',
    'achievements', 'certifications', 'internship', 'bachelor', 'master', 'gpa',
    'university', 'college', 'worked', 'developed', 'implemented', 'managed',
    'led', 'created', 'designed', 'built', 'improved', 'increased', 'reduced',
]


def extract_text_from_resume(file_path):
    """Extract text from uploaded resume (PDF simulation for demo)."""
    # In production, use PyPDF2 or pdfminer.six
    # For demo, generate mock content
    sample_texts = [
        """John Doe | Software Engineer | john@example.com | +91-9876543210 | LinkedIn | GitHub
        
        SUMMARY
        Enthusiastic software engineer with 2 years of experience in Python, Django, React.
        Strong understanding of web technologies and cloud platforms.
        
        EDUCATION
        B.Tech Computer Science | ABC University | 2022 | CGPA: 8.5/10
        
        TECHNICAL SKILLS
        Python, Django, Flask, JavaScript, React, HTML, CSS, SQL, MySQL, PostgreSQL,
        Git, GitHub, Docker, AWS, Machine Learning basics, REST APIs, Agile
        
        EXPERIENCE
        Software Developer Intern | XYZ Company | June 2022 - Dec 2022
        - Developed RESTful APIs using Django and Python
        - Built responsive UI components with React and Bootstrap
        - Managed database schemas with PostgreSQL
        - Worked in Agile team with 5 developers
        
        PROJECTS
        1. E-Commerce Platform - Django, React, PostgreSQL, Stripe API
        2. ML-Based Recommendation System - Python, Scikit-learn, Pandas
        3. Real-time Chat App - Node.js, WebSockets, MongoDB
        
        CERTIFICATIONS
        AWS Cloud Practitioner | Python for Data Science - Coursera | Web Development Bootcamp
        
        ACHIEVEMENTS
        - Top 5% in University Technical Fest 2022
        - Open source contributor with 50+ GitHub stars
        """,
    ]
    try:
        return sample_texts[0]
    except Exception:
        return ""


def extract_skills(text):
    """Extract skills from resume text."""
    text_lower = text.lower()
    found = []
    for category, skills in SKILL_CATEGORIES.items():
        for skill in skills:
            if skill in text_lower and skill not in found:
                found.append(skill)
    return found


def detect_role(text, skills):
    """Detect the most likely job role."""
    text_lower = text.lower()
    role_scores = {}
    for role, role_skills in ROLE_SKILL_MAP.items():
        score = sum(1 for s in role_skills if s in text_lower)
        role_scores[role] = score
    if role_scores:
        return max(role_scores, key=role_scores.get)
    return 'Software Engineer'


def get_missing_skills(detected_role, found_skills):
    """Get skills missing for the detected role."""
    role_skills = ROLE_SKILL_MAP.get(detected_role, [])
    found_lower = [s.lower() for s in found_skills]
    return [s for s in role_skills if s.lower() not in found_lower]


def calculate_ats_score(text, skills):
    """Calculate ATS compatibility score."""
    text_lower = text.lower()
    score = 0

    # Check ATS keywords (30%)
    keyword_hits = sum(1 for kw in ATS_KEYWORDS if kw in text_lower)
    score += min(30, int((keyword_hits / len(ATS_KEYWORDS)) * 30))

    # Section headings (25%)
    sections = ['education', 'experience', 'skills', 'projects', 'summary', 'certifications']
    section_hits = sum(1 for s in sections if s in text_lower)
    score += min(25, int((section_hits / len(sections)) * 25))

    # Skills count (25%)
    score += min(25, len(skills) * 2)

    # Contact info (20%)
    has_email = bool(re.search(r'[\w.-]+@[\w.-]+\.\w+', text))
    has_phone = bool(re.search(r'[\+\d][\d\s\-]{9,}', text))
    has_linkedin = 'linkedin' in text_lower
    contact_score = sum([has_email * 8, has_phone * 7, has_linkedin * 5])
    score += min(20, contact_score)

    return min(100, score)


def calculate_resume_score(text, skills, ats_score):
    """Calculate overall resume quality score."""
    text_lower = text.lower()
    scores = {}

    # Education (20%)
    edu_keywords = ['bachelor', 'master', 'b.tech', 'b.e', 'mba', 'university', 'college', 'gpa', 'cgpa']
    edu_hits = sum(1 for k in edu_keywords if k in text_lower)
    scores['education'] = min(100, edu_hits * 15)

    # Experience (25%)
    exp_action_words = ['developed', 'implemented', 'managed', 'led', 'created', 'designed',
                        'built', 'improved', 'reduced', 'increased', 'achieved', 'collaborated']
    exp_hits = sum(1 for w in exp_action_words if w in text_lower)
    has_numbers = bool(re.search(r'\d+%|\d+\s*(users|projects|team|members)', text_lower))
    scores['experience'] = min(100, (exp_hits * 7) + (20 if has_numbers else 0))

    # Skills (25%)
    scores['skills'] = min(100, len(skills) * 5)

    # Formatting (30%)
    word_count = len(text.split())
    format_score = 60 if 300 <= word_count <= 800 else 40
    format_score += 20 if 'summary' in text_lower or 'objective' in text_lower else 0
    format_score += 20 if 'projects' in text_lower else 0
    scores['formatting'] = min(100, format_score)

    overall = int(
        scores['education'] * 0.20 +
        scores['experience'] * 0.25 +
        scores['skills'] * 0.25 +
        scores['formatting'] * 0.30
    )

    return overall, scores


def generate_suggestions(text, skills, missing_skills, resume_score, ats_score):
    """Generate improvement suggestions."""
    suggestions = []
    text_lower = text.lower()

    if ats_score < 70:
        suggestions.append("⚡ Add more ATS-friendly keywords specific to your target job role.")
    if len(skills) < 8:
        suggestions.append("🛠️ List more technical skills — aim for 10-15 relevant skills.")
    if missing_skills:
        top_missing = ', '.join(missing_skills[:3])
        suggestions.append(f"📚 Consider learning: {top_missing} — high demand for your target role.")
    if not re.search(r'\d+%|\d+ (users|projects|people|team)', text_lower):
        suggestions.append("📊 Quantify your achievements with numbers (e.g., 'Improved performance by 30%').")
    if 'summary' not in text_lower and 'objective' not in text_lower:
        suggestions.append("✍️ Add a Professional Summary section at the top of your resume.")
    if 'linkedin' not in text_lower:
        suggestions.append("🔗 Include your LinkedIn profile URL for better recruiter visibility.")
    if 'github' not in text_lower and 'portfolio' not in text_lower:
        suggestions.append("💻 Add your GitHub or portfolio link to showcase projects.")
    if len(text.split()) < 300:
        suggestions.append("📝 Your resume seems short. Expand your experience and project sections.")
    if resume_score < 60:
        suggestions.append("🎯 Use strong action verbs (Led, Built, Optimized, Delivered) to start bullet points.")
    if 'certifications' not in text_lower:
        suggestions.append("🏆 Add relevant certifications to stand out from other candidates.")

    return suggestions[:7]


def analyze_resume(resume_instance):
    """Main function to analyze a resume."""
    from .models import ResumeAnalysis

    try:
        text = extract_text_from_resume(resume_instance.file.path)
        skills = extract_skills(text)
        detected_role = detect_role(text, skills)
        missing_skills = get_missing_skills(detected_role, skills)
        ats_score = calculate_ats_score(text, skills)
        resume_score, sub_scores = calculate_resume_score(text, skills, ats_score)
        suggestions = generate_suggestions(text, skills, missing_skills, resume_score, ats_score)

        exp_level = 'Fresher'
        if 'senior' in text.lower() or '5 year' in text.lower():
            exp_level = 'Senior'
        elif 'intern' in text.lower() or '1 year' in text.lower() or '2 year' in text.lower():
            exp_level = 'Junior'
        elif '3 year' in text.lower() or '4 year' in text.lower():
            exp_level = 'Mid-Level'

        analysis, _ = ResumeAnalysis.objects.update_or_create(
            resume=resume_instance,
            defaults={
                'resume_score': resume_score,
                'ats_score': ats_score,
                'extracted_skills': skills,
                'missing_skills': missing_skills,
                'improvement_suggestions': suggestions,
                'education_score': sub_scores.get('education', 0),
                'experience_score': sub_scores.get('experience', 0),
                'skills_score': sub_scores.get('skills', 0),
                'formatting_score': sub_scores.get('formatting', 0),
                'detected_role': detected_role,
                'experience_level': exp_level,
                'raw_text': text[:2000],
            }
        )

        resume_instance.status = 'completed'
        resume_instance.save()
        return analysis

    except Exception as e:
        resume_instance.status = 'failed'
        resume_instance.save()
        raise e