from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from .models import CustomUser
from adminControl.models import General
from .forms import CustomUserCreationForm , ProfileUpdateForm
from adminControl.forms import GeneralForm
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        registerForm = CustomUserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Account creation failed')
            return redirect('register')
    else:
        registerForm = CustomUserCreationForm()

    form = GeneralForm(instance=General.objects.first())

    context = {
        'registerForm': registerForm,
        'form': form,
    }
    return render(request, 'adminControl/adminCreation/register.html', context=context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = GeneralForm(instance=General.objects.first())
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
        
    return render(request, 'adminControl/adminCreation/login.html' , {'form': form})



@login_required
def update_profile(request):
    if request.method == 'POST':
        updateForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if 'profile_image' in request.FILES:
            file = request.FILES['profile_image']
            if file.size > 1 * 1024 * 1024: 
                messages.error(request, 'File size exceeds 1MB. Please upload a smaller image.')
                return redirect('update_profile')
            
        if updateForm.is_valid():
            updateForm.save()
            messages.success(request, 'Profile updated successfully')
            next_url = request.POST.get('next')
            return redirect(next_url)
        else:
            messages.error(request, 'Profile update failed')
            return redirect('update_profile')
    else:
        updateForm = ProfileUpdateForm(instance=request.user)

    context = {
        'updateForm': updateForm,
    }

    return render(request, 'adminControl/dashboard/dashboard.html' , context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def send_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'snrredoy2@gmail.com',
        ['snrredoy3@gmail.com'],
        fail_silently=False,
    )

    return messages.success('Email sent successfully!')