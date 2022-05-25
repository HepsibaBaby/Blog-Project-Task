from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from BlogApp.forms import ProfileForm
from BlogApp.models import Profile


def home(request):
    return render(request, 'Admin/index.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('adminview')
        else:
            messages.info(request, 'Invalid credentials')
    return render(request, 'Admin/login.html')

def adminhome(request):
    return render(request, 'Admin/adminhome.html')

def profile_add(request):
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profileview')
    return render(request, 'Admin/profile_add.html',{'profile_form':profile_form})

def profile_view(request):
    profile = Profile.objects.all()
    return render(request, 'Admin/profile_view.html', {'profile':profile})





