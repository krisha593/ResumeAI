from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile


# ─── LOGIN VIEW ───────────────────────────────────────────────────────────────
def login_view(request):
    # If user is already logged in, send to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'accounts/login.html')


# ─── REGISTER VIEW ────────────────────────────────────────────────────────────
def register_view(request):
    # If user is already logged in, send to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        first_name       = request.POST.get('first_name', '').strip()
        last_name        = request.POST.get('last_name', '').strip()
        username         = request.POST.get('username', '').strip()
        email            = request.POST.get('email', '').strip()
        password         = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # ── Validations ──
        if not first_name or not username or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'accounts/register.html')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'accounts/register.html')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose a different one.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered. Please login instead.')
            return render(request, 'accounts/register.html')

        # ── Create User ──
        try:
            user = User.objects.create_user(
                username   = username,
                email      = email,
                password   = password,
                first_name = first_name,
                last_name  = last_name
            )
            # Create the UserProfile too
            UserProfile.objects.get_or_create(user=user)

            # Auto login after registration
            login(request, user)
            messages.success(request, f'Welcome to ResumeAI, {first_name}! Your account is ready.')
            return redirect('dashboard')

        except Exception as e:
            messages.error(request, 'Something went wrong. Please try again.')
            return render(request, 'accounts/register.html')

    return render(request, 'accounts/register.html')


# ─── LOGOUT VIEW ──────────────────────────────────────────────────────────────
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


# ─── PROFILE VIEW ─────────────────────────────────────────────────────────────
@login_required
def profile_view(request):
    # Get or create profile for this user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':

        # ── Update User model fields ──
        request.user.first_name = request.POST.get('first_name', '').strip()
        request.user.last_name  = request.POST.get('last_name', '').strip()
        request.user.email      = request.POST.get('email', '').strip()
        request.user.save()

        # ── Update UserProfile fields ──
        profile.phone            = request.POST.get('phone', '').strip()
        profile.bio              = request.POST.get('bio', '').strip()
        profile.location         = request.POST.get('location', '').strip()
        profile.linkedin         = request.POST.get('linkedin', '').strip()
        profile.github           = request.POST.get('github', '').strip()
        profile.desired_role     = request.POST.get('desired_role', '').strip()

        # Experience years — default to 0 if empty
        exp = request.POST.get('experience_years', '0')
        profile.experience_years = int(exp) if exp.isdigit() else 0

        # ── Handle profile picture upload ──
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    # GET request — just show the profile form
    return render(request, 'accounts/profile.html', {
        'profile': profile
    })