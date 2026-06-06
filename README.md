\# ResumeAI — AI-Powered Resume Analyzer \& Job Recommendation System



> 🎓 College Major Project | Built with Django, Python, Bootstrap 5



\---



\## 📌 Project Overview



ResumeAI is a full-stack web application that uses AI algorithms to analyze resumes, calculate ATS compatibility scores, extract skills, and provide personalized job and course recommendations.



\---



\## 🚀 Features



\- ✅ AI Resume Scoring (0–100)

\- ✅ ATS Compatibility Score

\- ✅ Skill Extraction \& Gap Detection

\- ✅ Job Recommendations with Match %

\- ✅ Course Recommendations

\- ✅ User Dashboard with Analytics

\- ✅ Admin Dashboard

\- ✅ PDF Upload with Drag \& Drop

\- ✅ User Authentication (Register/Login/Logout)

\- ✅ User Profile Management

\- ✅ Responsive Dark UI (Blue/Purple Theme)



\---



\## 🛠️ Tech Stack



| Technology | Purpose |

|-----------|---------|

| Python 3.10+ | Backend Language |

| Django 6.x | Web Framework |

| SQLite | Database |

| Bootstrap 5 | Frontend UI |

| JavaScript | Interactivity |

| HTML5 / CSS3 | Templates |

| Bootstrap Icons | Icons |



\---



\## 📁 Project Structure



```

ResumeAI/

│

├── manage.py

├── db.sqlite3

├── requirements.txt

│

├── resumeai\_project/          # Django project config

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

│

├── accounts/                  # User auth \& profiles

│   ├── models.py              # UserProfile model

│   ├── views.py               # Login, Register, Profile

│   ├── urls.py

│   ├── signals.py             # Auto profile creation

│   └── admin.py

│

├── analyzer/                  # Resume analysis engine

│   ├── models.py              # Resume, ResumeAnalysis models

│   ├── views.py               # Upload, Analysis views

│   ├── utils.py               # AI scoring algorithms

│   └── urls.py

│

├── jobs/                      # Job \& course recommendations

│   ├── models.py              # JobRecommendation, CourseRecommendation

│   ├── views.py

│   ├── utils.py               # Recommendation engine

│   └── urls.py

│

├── dashboard/                 # Dashboard views

│   ├── views.py               # User \& Admin dashboards

│   └── urls.py

│

├── templates/                 # All HTML templates

│   ├── base.html              # Base layout

│   ├── home.html              # Landing page

│   ├── about.html

│   ├── contact.html

│   ├── partials/

│   │   ├── navbar.html

│   │   └── footer.html

│   ├── accounts/

│   │   ├── login.html

│   │   ├── register.html

│   │   └── profile.html

│   ├── analyzer/

│   │   ├── upload.html

│   │   ├── analysis.html

│   │   └── list.html

│   ├── jobs/

│   │   ├── jobs.html

│   │   └── courses.html

│   └── dashboard/

│       ├── dashboard.html

│       └── admin\_dashboard.html

│

├── static/                    # CSS, JS, Images

└── media/                     # Uploaded resumes \& profile pics

```



\---



\## ⚙️ Installation \& Setup



\### Prerequisites

\- Python 3.10 or higher

\- pip (Python package manager)

\- Git (optional)



\### Step 1 — Clone or Download the Project

```bash

\# Option A: Clone with Git

git clone https://github.com/yourusername/ResumeAI.git

cd ResumeAI



\# Option B: Download ZIP and extract, then open terminal in folder

cd C:\\Users\\YourName\\Desktop\\ResumeAI

```



\### Step 2 — Create Virtual Environment

```bash

\# Windows

python -m venv venv

venv\\Scripts\\activate



\# Mac/Linux

python -m venv venv

source venv/bin/activate

```



\### Step 3 — Install Dependencies

```bash

pip install django pillow

```



\### Step 4 — Run Database Migrations

```bash

python manage.py makemigrations accounts

python manage.py makemigrations analyzer

python manage.py makemigrations jobs

python manage.py makemigrations dashboard

python manage.py migrate

```



\### Step 5 — Create Admin Account

```bash

python manage.py createsuperuser

```

Enter username, email, and password when prompted.



\### Step 6 — Start the Server

```bash

python manage.py runserver

```



\### Step 7 — Open in Browser

```

http://127.0.0.1:8000/

```



\---



\## 🌐 All Pages \& URLs



| Page | URL |

|------|-----|

| 🏠 Home | `http://127.0.0.1:8000/` |

| ℹ️ About | `http://127.0.0.1:8000/about/` |

| 📞 Contact | `http://127.0.0.1:8000/contact/` |

| 📝 Register | `http://127.0.0.1:8000/accounts/register/` |

| 🔑 Login | `http://127.0.0.1:8000/accounts/login/` |

| 👤 Profile | `http://127.0.0.1:8000/accounts/profile/` |

| 📊 Dashboard | `http://127.0.0.1:8000/dashboard/` |

| 📄 Upload Resume | `http://127.0.0.1:8000/analyzer/upload/` |

| 🔍 My Analyses | `http://127.0.0.1:8000/analyzer/history/` |

| 💼 Job Matches | `http://127.0.0.1:8000/jobs/recommendations/` |

| 🎓 Courses | `http://127.0.0.1:8000/jobs/courses/` |

| 🛡️ Admin Panel | `http://127.0.0.1:8000/admin-panel/` |

| ⚙️ Django Admin | `http://127.0.0.1:8000/admin/` |



\---



\## 🗄️ Database Models



\### UserProfile

| Field | Type | Description |

|-------|------|-------------|

| user | OneToOne | Links to Django User |

| phone | CharField | Phone number |

| bio | TextField | About the user |

| location | CharField | City/Country |

| linkedin | URLField | LinkedIn URL |

| github | URLField | GitHub URL |

| desired\_role | CharField | Target job role |

| experience\_years | IntegerField | Years of experience |



\### Resume

| Field | Type | Description |

|-------|------|-------------|

| user | ForeignKey | Owner of resume |

| file | FileField | PDF file path |

| original\_filename | CharField | Original file name |

| status | CharField | pending/analyzing/completed/failed |

| uploaded\_at | DateTimeField | Upload timestamp |



\### ResumeAnalysis

| Field | Type | Description |

|-------|------|-------------|

| resume | OneToOne | Linked resume |

| resume\_score | IntegerField | Overall score 0-100 |

| ats\_score | IntegerField | ATS score 0-100 |

| extracted\_skills | JSONField | List of detected skills |

| missing\_skills | JSONField | Skills needed for role |

| improvement\_suggestions | JSONField | AI tips list |

| education\_score | IntegerField | Education section score |

| experience\_score | IntegerField | Experience section score |

| skills\_score | IntegerField | Skills section score |

| formatting\_score | IntegerField | Formatting score |

| detected\_role | CharField | AI-detected job role |

| experience\_level | CharField | Fresher/Junior/Mid/Senior |



\### JobRecommendation

| Field | Type | Description |

|-------|------|-------------|

| user | ForeignKey | Recommendation owner |

| title | CharField | Job title |

| company | CharField | Company name |

| location | CharField | Job location |

| match\_percentage | IntegerField | Skills match % |

| salary\_range | CharField | Salary info |

| required\_skills | JSONField | Skills needed |



\### CourseRecommendation

| Field | Type | Description |

|-------|------|-------------|

| user | ForeignKey | Recommendation owner |

| title | CharField | Course name |

| provider | CharField | Udemy/Coursera etc |

| skill\_covered | CharField | Skill it teaches |

| level | CharField | Beginner/Intermediate/Advanced |

| rating | FloatField | Course rating |

| is\_free | BooleanField | Free or paid |



\---



\## 🤖 AI Analysis Engine



The resume analysis uses keyword-based scoring algorithms:



\### Scoring Breakdown

\- \*\*Education Score (20%)\*\* — Detects degree, university, GPA keywords

\- \*\*Experience Score (25%)\*\* — Counts action verbs, quantified achievements

\- \*\*Skills Score (25%)\*\* — Number of recognized technical skills

\- \*\*Formatting Score (30%)\*\* — Sections, word count, structure



\### ATS Score Calculation

\- Keyword presence (30%)

\- Section headings (25%)

\- Skills count (25%)

\- Contact information (20%)



\### Skill Categories Detected

\- Programming: Python, Java, JavaScript, C++, etc.

\- Web: React, Django, Node.js, HTML, CSS, etc.

\- Data Science: ML, TensorFlow, Pandas, SQL, etc.

\- Cloud: AWS, Docker, Kubernetes, Git, etc.

\- Database: MySQL, PostgreSQL, MongoDB, etc.

\- Soft Skills: Leadership, Agile, Communication, etc.



\---



\## 🔧 Optional: Enable Real PDF Parsing



By default the system uses demo text. To analyze actual PDF content:



```bash

pip install PyPDF2

```



Then in `analyzer/utils.py`, the `extract\_text\_from\_resume()` function automatically tries PyPDF2 first.



\---



\## 👥 User Roles



| Role | Access |

|------|--------|

| Regular User | Register, upload resume, view analysis, job/course recommendations |

| Staff/Admin | All of above + Admin Dashboard at `/admin-panel/` |

| Superuser | All of above + Django Admin at `/admin/` |



\---



\## 🎨 UI Design



\- \*\*Theme:\*\* Dark mode with Blue/Purple gradient (#5B4CF5 → #8B5CF6 → #06B6D4)

\- \*\*Framework:\*\* Bootstrap 5.3

\- \*\*Layout:\*\* Fixed sidebar for authenticated users, sticky navbar for public pages

\- \*\*Font:\*\* Plus Jakarta Sans + Sora

\- \*\*Icons:\*\* Bootstrap Icons 1.11



\---



\## 🐛 Common Issues \& Fixes



| Error | Fix |

|-------|-----|

| `ModuleNotFoundError: django` | Run `pip install django` inside venv |

| `Table does not exist` | Run `python manage.py migrate` |

| `TemplateDoesNotExist` | Check `TEMPLATES DIRS` in settings.py |

| Port already in use | Run `python manage.py runserver 8080` |

| `No module named PIL` | Run `pip install pillow` |

| Page shows blank | Press `Ctrl+Shift+R` to hard refresh browser |



\---



\## 📊 Project Stats



\- \*\*Total Pages:\*\* 12

\- \*\*Django Apps:\*\* 4 (accounts, analyzer, jobs, dashboard)

\- \*\*Database Models:\*\* 5

\- \*\*AI Skill Categories:\*\* 6

\- \*\*Job Database:\*\* 10+ job types

\- \*\*Course Database:\*\* 10+ courses



\---



\## 🏫 Academic Information



\- \*\*Project Type:\*\* College Major Project (MVP)

\- \*\*Department:\*\* Computer Science \& Engineering

\- \*\*Technology:\*\* Django Full Stack Web Development

\- \*\*Database:\*\* SQLite (Development)



\---



\## 📄 License



This project is built for educational purposes as a college major project.



\---



\## 🙏 Acknowledgments



\- Django Documentation

\- Bootstrap 5 Framework

\- Bootstrap Icons

\- Google Fonts (Plus Jakarta Sans, Sora)



\---



\*Built with ❤️ using Django \& Python\*





