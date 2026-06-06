html = """{% extends 'base.html' %}
{% block title %}ResumeAI - AI Powered Resume Analyzer{% endblock %}
{% block content %}
<style>
body{background:#0D0C1E!important}
.hero{min-height:93vh;display:flex;align-items:center;position:relative;overflow:hidden;padding:60px 0}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 55% at 50% 15%,rgba(91,76,245,.18) 0%,transparent 65%)}
.grad-t{background:linear-gradient(135deg,#5B4CF5,#8B5CF6,#06B6D4);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.feat-card{background:#161528;border:1px solid rgba(255,255,255,.06);border-radius:20px;padding:28px;transition:all .3s;height:100%}
.feat-card:hover{transform:translateY(-5px);border-color:rgba(91,76,245,.3);box-shadow:0 18px 52px rgba(0,0,0,.35)}
.feat-icon{width:54px;height:54px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:16px}
.step-n{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,#5B4CF5,#8B5CF6);display:flex;align-items:center;justify-content:center;font-family:'Sora',sans-serif;font-weight:800;font-size:17px;color:#fff;flex-shrink:0}
.preview-card{background:rgba(22,21,40,.85);border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:26px;backdrop-filter:blur(20px)}
.btn-main{background:linear-gradient(135deg,#5B4CF5,#8B5CF6);color:#fff;border:none;border-radius:12px;padding:13px 30px;font-size:14.5px;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:all .25s}
.btn-main:hover{transform:translateY(-2px);box-shadow:0 12px 36px rgba(91,76,245,.4);color:#fff}
.btn-ghost{background:transparent;color:rgba(255,255,255,.75);border:1px solid rgba(255,255,255,.13);border-radius:12px;padding:13px 30px;font-size:14.5px;font-weight:500;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:all .25s}
.btn-ghost:hover{background:rgba(255,255,255,.05);color:#fff}
</style>

<!-- HERO -->
<section class="hero">
<div class="container position-relative">
<div class="row align-items-center g-5">
  <div class="col-lg-6">
    <div style="display:inline-flex;align-items:center;gap:7px;padding:5px 15px;border-radius:20px;background:rgba(91,76,245,.13);border:1px solid rgba(91,76,245,.28);font-size:11.5px;font-weight:700;color:#A78BFA;text-transform:uppercase;letter-spacing:1.1px;margin-bottom:20px">
      <i class="bi bi-stars"></i> AI-Powered Career Platform
    </div>
    <h1 style="font-family:'Sora',sans-serif;font-size:clamp(34px,5.5vw,68px);font-weight:800;line-height:1.08;margin-bottom:20px">
      Get Your Resume<br/><span class="grad-t">Scored by AI.</span><br/>Land Dream Jobs.
    </h1>
    <p style="font-size:16px;color:rgba(255,255,255,.55);line-height:1.75;max-width:480px;margin-bottom:30px">
      Upload your resume and instantly get an AI analysis — ATS score, skill gaps, job matches, and learning recommendations.
    </p>
    <div class="d-flex flex-wrap gap-3 mb-5">
      <a href="{% url 'register' %}" class="btn-main"><i class="bi bi-rocket-takeoff-fill"></i> Get Started Free</a>
      <a href="{% url 'about' %}" class="btn-ghost"><i class="bi bi-play-circle-fill"></i> Learn More</a>
    </div>
    <div class="d-flex gap-5">
      <div><div style="font-family:'Sora',sans-serif;font-size:36px;font-weight:800" class="grad-t">500+</div><div style="font-size:12.5px;color:rgba(255,255,255,.35)">Resumes Analyzed</div></div>
      <div><div style="font-family:'Sora',sans-serif;font-size:36px;font-weight:800" class="grad-t">95%</div><div style="font-size:12.5px;color:rgba(255,255,255,.35)">ATS Accuracy</div></div>
      <div><div style="font-family:'Sora',sans-serif;font-size:36px;font-weight:800" class="grad-t">50+</div><div style="font-size:12.5px;color:rgba(255,255,255,.35)">Job Categories</div></div>
    </div>
  </div>
  <div class="col-lg-6">
    <div class="preview-card">
      <div class="d-flex align-items-center justify-content-between mb-4">
        <div>
          <div style="font-family:'Sora',sans-serif;font-weight:700;font-size:15px">Resume Analysis</div>
          <div style="font-size:11.5px;color:rgba(255,255,255,.35)">john_resume_2024.pdf</div>
        </div>
        <span style="background:rgba(16,185,129,.13);color:#6EE7B7;border:1px solid rgba(16,185,129,.28);padding:4px 11px;border-radius:20px;font-size:11.5px;font-weight:700">Analyzed</span>
      </div>
      <div class="row g-3 mb-4">
        <div class="col-6">
          <div style="background:rgba(91,76,245,.1);border:1px solid rgba(91,76,245,.2);border-radius:12px;padding:18px;text-align:center">
            <div style="font-size:38px;font-weight:800;font-family:'Sora',sans-serif" class="grad-t">78</div>
            <div style="font-size:10.5px;color:rgba(255,255,255,.35);text-transform:uppercase;letter-spacing:1px">Resume Score</div>
          </div>
        </div>
        <div class="col-6">
          <div style="background:rgba(6,182,212,.1);border:1px solid rgba(6,182,212,.2);border-radius:12px;padding:18px;text-align:center">
            <div style="font-size:38px;font-weight:800;font-family:'Sora',sans-serif;color:#67E8F9">82</div>
            <div style="font-size:10.5px;color:rgba(255,255,255,.35);text-transform:uppercase;letter-spacing:1px">ATS Score</div>
          </div>
        </div>
      </div>
      <div class="mb-3">
        <div class="d-flex justify-content-between mb-1" style="font-size:12.5px"><span>Skills Match</span><span style="color:#A78BFA;font-weight:700">85%</span></div>
        <div style="height:6px;background:rgba(255,255,255,.05);border-radius:6px"><div style="height:100%;width:85%;background:linear-gradient(135deg,#5B4CF5,#8B5CF6);border-radius:6px"></div></div>
      </div>
      <div class="mb-3">
        <div class="d-flex justify-content-between mb-1" style="font-size:12.5px"><span>ATS Compatibility</span><span style="color:#67E8F9;font-weight:700">82%</span></div>
        <div style="height:6px;background:rgba(255,255,255,.05);border-radius:6px"><div style="height:100%;width:82%;background:linear-gradient(135deg,#06B6D4,#3B82F6);border-radius:6px"></div></div>
      </div>
      <div style="font-size:11px;color:rgba(255,255,255,.35);margin-bottom:8px;text-transform:uppercase;letter-spacing:1px">Detected Skills</div>
      <div>
        <span class="skill-badge">Python</span>
        <span class="skill-badge">Django</span>
        <span class="skill-badge">React</span>
        <span class="skill-badge">SQL</span>
        <span class="skill-badge">Docker</span>
        <span class="skill-badge">Git</span>
        <span class="skill-badge">AWS</span>
      </div>
    </div>
  </div>
</div>
</div>
</section>

<!-- FEATURES -->
<section style="padding:90px 0">
<div class="container">
  <div class="text-center mb-5">
    <h2 style="font-family:'Sora',sans-serif;font-weight:800;font-size:clamp(26px,3.5vw,42px)">Everything You Need to <span class="grad-t">Advance Your Career</span></h2>
  </div>
  <div class="row g-4">
    <div class="col-md-6 col-lg-4"><div class="feat-card"><div class="feat-icon" style="background:rgba(91,76,245,.12)">🔍</div><h5 style="font-family:'Sora',sans-serif;font-weight:700;margin-bottom:10px">Deep Resume Analysis</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">AI scans every section — skills, experience, education, and formatting to give a comprehensive quality score.</p></div></div>
    <div class="col-md-6 col-lg-4"><div class="feat-card"><div class="feat-icon" style="background:rgba(6,182,212,.1)">🤖</div><h5 style="font-family:'Sora',sans-serif;font-weight:700;margin-bottom:10px">ATS Score Check</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Know exactly how your resume performs in Applicant Tracking Systems used by top companies worldwide.</p></div></div>
    <div class="col-md-6 col-lg-4"><div class="feat-card"><div class="feat-icon" style="background:rgba(16,185,129,.1)">💼</div><h5 style="font-family:'Sora',sans-serif;font-weight:700;margin-bottom:10px">Smart Job Matching</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Get personalized job recommendations with match percentages based on your unique skill profile.</p></div></div>
    <div class="col-md-6 col-lg-4"><div class="feat-card"><div class="feat-icon" style="background:rgba(245,158,11,.1)">📚</div><h5 style="font-family:'Sora',sans-serif;font-weight:700;margin-bottom:10px">Course Recommendations</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Bridge skill gaps with curated courses from Udemy, Coursera, and top learning platforms.</p></div></div>
    <div class="col-md-6 col-lg-4"><div class="feat-card"><div class="feat-icon" style="background:rgba(139,92,246,.1)">⚡</div><h5 style="font-family:'Sora',sans-serif;font-weight:700;margin-bottom:10px">Instant Results</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Get your complete AI analysis in under 10 seconds. No waiting, no manual process required.</p></div></div>
    <div class="col-md-6 col-lg-4"><div class="feat-card"><div class="feat-icon" style="background:rgba(239,68,68,.08)">📈</div><h5 style="font-family:'Sora',sans-serif;font-weight:700;margin-bottom:10px">Actionable Tips</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Get specific, actionable suggestions to improve your resume and maximize interview callback rates.</p></div></div>
  </div>
</div>
</section>

<!-- HOW IT WORKS -->
<section style="padding:90px 0;background:rgba(22,21,40,.4)">
<div class="container">
  <div class="text-center mb-5">
    <h2 style="font-family:'Sora',sans-serif;font-weight:800;font-size:clamp(26px,3.5vw,40px)">How It <span class="grad-t">Works</span></h2>
    <p style="color:rgba(255,255,255,.4);font-size:15px;margin-top:10px">3 simple steps to transform your career</p>
  </div>
  <div class="row g-4 justify-content-center">
    <div class="col-md-4">
      <div class="d-flex gap-3">
        <div class="step-n">1</div>
        <div><h5 style="font-weight:700;margin-bottom:8px">Upload Your Resume</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Drag and drop or upload your PDF resume. Supports all standard formats up to 5MB.</p></div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="d-flex gap-3">
        <div class="step-n">2</div>
        <div><h5 style="font-weight:700;margin-bottom:8px">AI Analyzes It</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Our AI engine extracts skills, scores each section, detects your role, and checks ATS compatibility.</p></div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="d-flex gap-3">
        <div class="step-n">3</div>
        <div><h5 style="font-weight:700;margin-bottom:8px">Get Recommendations</h5><p style="color:rgba(255,255,255,.45);font-size:13.5px;line-height:1.7">Receive matched jobs, course suggestions, and specific tips to improve your resume score.</p></div>
      </div>
    </div>
  </div>
</div>
</section>

<!-- CTA -->
<section style="padding:90px 0">
<div class="container">
  <div style="background:linear-gradient(135deg,rgba(91,76,245,.18),rgba(139,92,246,.12),rgba(6,182,212,.08));border:1px solid rgba(91,76,245,.22);border-radius:24px;padding:64px;text-align:center">
    <h2 style="font-family:'Sora',sans-serif;font-weight:800;font-size:clamp(22px,3.5vw,38px);margin-bottom:14px">Ready to Supercharge <span class="grad-t">Your Career?</span></h2>
    <p style="color:rgba(255,255,255,.45);font-size:15.5px;max-width:460px;margin:0 auto 30px">Join hundreds of students using ResumeAI to get noticed by top employers. Free forever.</p>
    <a href="{% url 'register' %}" class="btn-main" style="font-size:15px;padding:15px 38px"><i class="bi bi-rocket-takeoff-fill"></i> Analyze My Resume Free</a>
  </div>
</div>
</section>
{% endblock %}"""

with open('templates/home.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("home.html fixed!")