from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

@login_required
def dashboard_view(request):
    user = request.user
    if user.user_type == 'doctor':
        return render(request, 'accounts/doctor_dashboard.html', {'user': user})
    elif user.user_type == 'patient':
        return render(request, 'accounts/patient_dashboard.html', {'user': user})
