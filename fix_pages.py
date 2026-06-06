import os

# Fix contact.html
contact = """{% extends 'base.html' %}
{% block title %}Contact - ResumeAI{% endblock %}
{% block content %}
<div style="padding:80px 0;min-height:80vh">
  <div class="container" style="max-width:600px">
    <div class="text-center mb-5">
      <h1 style="font-weight:800;font-size:38px;background:linear-gradient(135deg,#5B4CF5,#8B5CF6,#06B6D4);-webkit-background-clip:text;-webkit-text-fill-color:transparent">Contact Us</h1>
      <p style="color:rgba(255,255,255,.5);font-size:15px;margin-top:10px">Have questions? We would love to hear from you.</p>
    </div>
    <div style="background:#161528;border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:36px">
      <div class="mb-3">
        <label style="font-size:13px;font-weight:600;color:rgba(255,255,255,.6);margin-bottom:6px;display:block">Your Name</label>
        <input type="text" class="form-control" placeholder="John Doe" style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:10px;color:#fff;padding:11px 15px;font-size:14px"/>
      </div>
      <div class="mb-3">
        <label style="font-size:13px;font-weight:600;color:rgba(255,255,255,.6);margin-bottom:6px;display:block">Email</label>
        <input type="email" class="form-control" placeholder="john@example.com" style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:10px;color:#fff;padding:11px 15px;font-size:14px"/>
      </div>
      <div class="mb-3">
        <label style="font-size:13px;font-weight:600;color:rgba(255,255,255,.6);margin-bottom:6px;display:block">Subject</label>
        <input type="text" class="form-control" placeholder="Project inquiry..." style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:10px;color:#fff;padding:11px 15px;font-size:14px"/>
      </div>
      <div class="mb-4">
        <label style="font-size:13px;font-weight:600;color:rgba(255,255,255,.6);margin-bottom:6px;display:block">Message</label>
        <textarea class="form-control" rows="5" placeholder="Your message..." style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:10px;color:#fff;padding:11px 15px;font-size:14px;resize:none"></textarea>
      </div>
      <button class="btn btn-g w-100" onclick="alert('Message sent! Thank you.')">
        <i class="bi bi-send-fill me-2"></i>Send Message
      </button>
      <hr style="border-color:rgba(255,255,255,.07);margin:24px 0"/>
      <p style="color:rgba(255,255,255,.4);font-size:13px;text-align:center">
        📧 resumeai@college.edu &nbsp;|&nbsp; 📍 CS Department, XYZ University
      </p>
    </div>
  </div>
</div>
{% endblock %}"""

with open('templates/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact)
print("contact.html fixed!")

# Fix about.html
about = """{% extends 'base.html' %}
{% block title %}About - ResumeAI{% endblock %}
{% block content %}
<div style="padding:80px 0;min-height:80vh">
  <div class="container" style="max-width:800px">
    <div class="text-center mb-5">
      <h1 style="font-weight:800;font-size:38px;background:linear-gradient(135deg,#5B4CF5,#8B5CF6,#06B6D4);-webkit-background-clip:text;-webkit-text-fill-color:transparent">About ResumeAI</h1>
      <p style="color:rgba(255,255,255,.5);font-size:15px;margin-top:10px">A college major project built to help students land their dream jobs</p>
    </div>
    <div style="background:#161528;border:1px solid rgba(255,255,255,.07);border-radius:20px;padding:36px;margin-bottom:22px">
      <h4 style="font-weight:700;margin-bottom:14px">🎯 Project Overview</h4>
      <p style="color:rgba(255,255,255,.55);line-height:1.8;font-size:15px">ResumeAI is an AI-powered resume analysis and job recommendation system built as a Major Project for the Computer Science Department. It helps students and professionals improve their resumes, understand ATS compatibility, and find matching job opportunities.</p>
    </div>
    <div style="background:#161528;border:1px solid rgba(255,255,255,.07);border-radius:20px;padding:36px;margin-bottom:22px">
      <h4 style="font-weight:700;margin-bottom:16px">🛠️ Tech Stack Used</h4>
      <div class="d-flex flex-wrap gap-2">
        <span class="skill-badge">Django</span>
        <span class="skill-badge">Python</span>
        <span class="skill-badge">SQLite</span>
        <span class="skill-badge">Bootstrap 5</span>
        <span class="skill-badge">JavaScript</span>
        <span class="skill-badge">HTML5</span>
        <span class="skill-badge">CSS3</span>
      </div>
    </div>
    <div style="background:#161528;border:1px solid rgba(255,255,255,.07);border-radius:20px;padding:36px">
      <h4 style="font-weight:700;margin-bottom:16px">✨ Key Features</h4>
      <ul style="color:rgba(255,255,255,.55);line-height:2;font-size:15px;padding-left:20px">
        <li>AI-powered resume scoring and analysis</li>
        <li>ATS compatibility check with detailed score</li>
        <li>Automatic skill extraction and gap detection</li>
        <li>Smart job recommendations with match percentage</li>
        <li>Course recommendations from top platforms</li>
        <li>Professional user dashboard with analytics</li>
        <li>Admin panel for system management</li>
      </ul>
    </div>
  </div>
</div>
{% endblock %}"""

with open('templates/about.html', 'w', encoding='utf-8') as f:
    f.write(about)
print("about.html fixed!")

# Fix home.html
home = """{% extends 'base.html' %}
{% block title %}ResumeAI - AI Powered Resume Analyzer{% endblock %}
{% block content %}
<style>
.grad-t{background:linear-gradient(135deg,#5B4CF5,#8B5CF6,#06B6D4);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.feat-card{background:#161528;border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:26px;transition:all .3s;height:100%}
.feat-card:hover{transform:translateY(-4px);border-color:rgba(91,76,245,.35)}
.btn-main{background:linear-gradient(135deg,#5B4CF5,#8B5CF6);color:#fff!important;border-radius:12px;padding:13px 28px;font-size:14px;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:8px;border:none}
.btn-ghost{background:transparent;color:rgba(255,255,255,.8)!important;border:1px solid rgba(255,255,255,.15);border-radius:12px;padding:13px 28px;font-size:14px;text-decoration:none;display:inline-flex;align-items:center;gap:8px}
.step-n{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#5B4CF5,#8B5CF6);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:16px;color:#fff;flex-shrink:0}
</style>

<!-- HERO -->
<section style="min-height:92vh;display:flex;align-items:center;padding:60px 0;background:radial-gradient(ellipse 80% 50% at 50% 15%,rgba(91,76,245,.15) 0%,transparent 65%)">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6">
        <div style="display:inline-flex;align-items:center;gap:7px;padding:5px 16px;border-radius:20px;background:rgba(91,76,245,.13);border:1px solid rgba(91,76,245,.3);font-size:11px;font-weight:700;color:#A78BFA;text-transform:uppercase;letter-spacing:1px;margin-bottom:22px">
          <i class="bi bi-stars"></i> AI-Powered Career Platform
        </div>
        <h1 style="font-size:clamp(32px,5vw,62px);font-weight:800;line-height:1.1;margin-bottom:20px">
          Get Your Resume<br/><span class="grad-t">Scored by AI.</span><br/>Land Dream Jobs.
        </h1>
        <p style="font-size:16px;color:rgba(255,255,255,.55);line-height:1.75;max-width:460px;margin-bottom:28px">
          Upload your PDF resume and get instant AI analysis — ATS score, skill gaps, job matches, and course recommendations.
        </p>
        <div class="d-flex flex-wrap gap-3 mb-5">
          <a href="{% url 'register' %}" class="btn-main">
            <i class="bi bi-rocket-takeoff-fill"></i> Get Started Free
          </a>
          <a href="{% url 'about' %}" class="btn-ghost">
            <i class="bi bi-play-circle-fill"></i> Learn More
          </a>
        </div>
        <div class="d-flex gap-4">
          <div>
            <div style="font-size:32px;font-weight:800" class="grad-t">500+</div>
            <div style="font-size:12px;color:rgba(255,255,255,.35)">Resumes Analyzed</div>
          </div>
          <div>
            <div style="font-size:32px;font-weight:800" class="grad-t">95%</div>
            <div style="font-size:12px;color:rgba(255,255,255,.35)">ATS Accuracy</div>
          </div>
          <div>
            <div style="font-size:32px;font-weight:800" class="grad-t">50+</div>
            <div style="font-size:12px;color:rgba(255,255,255,.35)">Job Categories</div>
          </div>
        </div>
      </div>
      <div class="col-lg-6">
        <div style="background:rgba(22,21,40,.9);border:1px solid rgba(255,255,255,.1);border-radius:20px;padding:26px">
          <div class="d-flex align-items-center justify-content-between mb-4">
            <div>
              <div style="font-weight:700;font-size:15px">Resume Analysis</div>
              <div style="font-size:11px;color:rgba(255,255,255,.35)">john_resume_2024.pdf</div>
            </div>
            <span style="background:rgba(16,185,129,.13);color:#6EE7B7;border:1px solid rgba(16,185,129,.28);padding:4px 12px;border-radius:20px;font-size:11px;font-weight:700">Analyzed</span>
          </div>
          <div class="row g-3 mb-3">
            <div class="col-6">
              <div style="background:rgba(91,76,245,.1);border:1px solid rgba(91,76,245,.2);border-radius:12px;padding:16px;text-align:center">
                <div style="font-size:36px;font-weight:800" class="grad-t">78</div>
                <div style="font-size:10px;color:rgba(255,255,255,.35);text-transform:uppercase;letter-spacing:1px">Resume Score</div>
              </div>
            </div>
            <div class="col-6">
              <div style="background:rgba(6,182,212,.1);border:1px solid rgba(6,182,212,.2);border-radius:12px;padding:16px;text-align:center">
                <div style="font-size:36px;font-weight:800;color:#67E8F9">82</div>
                <div style="font-size:10px;color:rgba(255,255,255,.35);text-transform:uppercase;letter-spacing:1px">ATS Score</div>
              </div>
            </div>
          </div>
          <div class="mb-2">
            <div class="d-flex justify-content-between mb-1" style="font-size:12px"><span>Skills Match</span><span style="color:#A78BFA;font-weight:700">85%</span></div>
            <div style="height:6px;background:rgba(255,255,255,.06);border-radius:6px"><div style="height:100%;width:85%;background:linear-gradient(135deg,#5B4CF5,#8B5CF6);border-radius:6px"></div></div>
          </div>
          <div class="mb-3">
            <div class="d-flex justify-content-between mb-1" style="font-size:12px"><span>ATS Compatibility</span><span style="color:#67E8F9;font-weight:700">82%</span></div>
            <div style="height:6px;background:rgba(255,255,255,.06);border-radius:6px"><div style="height:100%;width:82%;background:linear-gradient(135deg,#06B6D4,#3B82F6);border-radius:6px"></div></div>
          </div>
          <div style="font-size:10px;color:rgba(255,255,255,.35);margin-bottom:8px;text-transform:uppercase;letter-spacing:1px">Detected Skills</div>
          <div>
            <span class="skill-badge">Python</span>
            <span class="skill-badge">Django</span>
            <span class="skill-badge">React</span>
            <span class="skill-badge">SQL</span>
            <span class="skill-badge">Docker</span>
            <span class="skill-badge">Git</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section style="padding:80px 0">
  <div class="container">
    <div class="text-center mb-5">
      <h2 style="font-weight:800;font-size:clamp(24px,3.5vw,40px)">
        Everything You Need to <span class="grad-t">Advance Your Career</span>
      </h2>
    </div>
    <div class="row g-4">
      <div class="col-md-6 col-lg-4"><div class="feat-card"><div style="font-size:34px;margin-bottom:14px">🔍</div><h5 style="font-weight:700;margin-bottom:8px">Deep Resume Analysis</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">AI scans every section to give a comprehensive quality score out of 100.</p></div></div>
      <div class="col-md-6 col-lg-4"><div class="feat-card"><div style="font-size:34px;margin-bottom:14px">🤖</div><h5 style="font-weight:700;margin-bottom:8px">ATS Score Check</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Know how your resume performs in Applicant Tracking Systems at top companies.</p></div></div>
      <div class="col-md-6 col-lg-4"><div class="feat-card"><div style="font-size:34px;margin-bottom:14px">💼</div><h5 style="font-weight:700;margin-bottom:8px">Smart Job Matching</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Get job recommendations with match percentages based on your skills.</p></div></div>
      <div class="col-md-6 col-lg-4"><div class="feat-card"><div style="font-size:34px;margin-bottom:14px">📚</div><h5 style="font-weight:700;margin-bottom:8px">Course Recommendations</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Bridge skill gaps with courses from Udemy, Coursera and top platforms.</p></div></div>
      <div class="col-md-6 col-lg-4"><div class="feat-card"><div style="font-size:34px;margin-bottom:14px">⚡</div><h5 style="font-weight:700;margin-bottom:8px">Instant Results</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Complete AI analysis in under 10 seconds. No waiting required.</p></div></div>
      <div class="col-md-6 col-lg-4"><div class="feat-card"><div style="font-size:34px;margin-bottom:14px">📈</div><h5 style="font-weight:700;margin-bottom:8px">Improvement Tips</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Actionable suggestions to improve your resume and get more interviews.</p></div></div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section style="padding:80px 0;background:rgba(22,21,40,.4)">
  <div class="container">
    <div class="text-center mb-5">
      <h2 style="font-weight:800;font-size:clamp(24px,3.5vw,38px)">How It <span class="grad-t">Works</span></h2>
    </div>
    <div class="row g-4 justify-content-center">
      <div class="col-md-4"><div class="d-flex gap-3"><div class="step-n">1</div><div><h5 style="font-weight:700;margin-bottom:8px">Upload Resume</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Upload your PDF resume up to 5MB.</p></div></div></div>
      <div class="col-md-4"><div class="d-flex gap-3"><div class="step-n">2</div><div><h5 style="font-weight:700;margin-bottom:8px">AI Analyzes It</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">AI extracts skills, scores sections, checks ATS.</p></div></div></div>
      <div class="col-md-4"><div class="d-flex gap-3"><div class="step-n">3</div><div><h5 style="font-weight:700;margin-bottom:8px">Get Results</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Receive job matches, courses, and tips instantly.</p></div></div></div>
    </div>
  </div>
</section>

<!-- CTA -->
<section style="padding:80px 0">
  <div class="container">
    <div style="background:linear-gradient(135deg,rgba(91,76,245,.2),rgba(139,92,246,.12));border:1px solid rgba(91,76,245,.25);border-radius:22px;padding:60px;text-align:center">
      <h2 style="font-weight:800;font-size:clamp(20px,3vw,36px);margin-bottom:14px">
        Ready to Supercharge <span class="grad-t">Your Career?</span>
      </h2>
      <p style="color:rgba(255,255,255,.45);font-size:15px;max-width:440px;margin:0 auto 28px">
        Join hundreds of students using ResumeAI. Free to start, always.
      </p>
      <a href="{% url 'register' %}" class="btn-main" style="font-size:15px;padding:14px 36px">
        <i class="bi bi-rocket-takeoff-fill"></i> Analyze My Resume Free
      </a>
    </div>
  </div>
</section>
{% endblock %}"""

with open('templates/home.html', 'w', encoding='utf-8') as f:
    f.write(home)
print("home.html fixed!")
print("")
print("ALL DONE! Now run: python manage.py runserver")