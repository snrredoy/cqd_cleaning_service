from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from .models import CustomUser
from adminControl.models import General
from .forms import CustomUserCreationForm
from adminControl.forms import GeneralForm


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

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')





from django.core.mail import send_mail
def send_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'snrredoy2@gmail.com',
        ['snrredoy3@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('Email sent successfully!')