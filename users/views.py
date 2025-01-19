from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,  update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back ' + username + '!')
            return redirect('core:home')  
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'users/auth.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('users:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('users:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('users:register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        '''
        send_mail(
            'Welcome to our site',
            'Thank you for registering on our website.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        '''
        messages.success(request, "Registered successfully! Please check your email.")
        return redirect('users:login')

    return render(request, 'users/auth.html')


@login_required
def view_profile(request):
    
    context = {
        'username': request.user.username,
        'email': request.user.email,
    }
    return render(request, 'users/user_profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = request.user
        user.username = username
        user.email = email
        
        if password:
            update_session_auth_hash(request, user)  # Prevents logout after password change
        user.save()

        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('users:view_profile')

    return render(request, 'users/edit_profile.html')
