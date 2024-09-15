from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return render(request, 'index.html')

def add_reservation(request):
    return render(request, 'AddReservation.html')

def add_hotel(request):
    return render(request, 'AddHotel.html')


def Available(request):
    return render(request, 'AvailableHotels.html')

def view_reservations(request):
    return render(request, 'ViewReservation.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)

            if user.is_superuser:
                return render(request, 'admin_welcome.html', {'user': user})
            else:
                return render(request, 'user_welcome.html', {'user': user})
        else:

            messages.error(request, 'Invalid email or password')

    return render(request, 'index.html')

@login_required
def add_user_view(request):
    # Ensure only superusers can add new users
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add users.')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('userpass')
        confirm_password = request.POST.get('Confirm')
        role = request.POST.get('role')  # Get the selected role (admin or employee)

        # Validation
        if not username or not password or not role:
            messages.error(request, 'All fields are required.')
            return redirect('add_user')
        

        if password != confirm_password:
            messages.error(request, "Passwords don't match.")
            return redirect('add_user')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('add_user')

        # Create user and set is_superuser based on role
        if role == 'admin':
            user = User.objects.create_user(username=username, password=password, is_superuser=True, is_staff=True)
        else:
            user = User.objects.create_user(username=username, password=password, is_superuser=False, is_staff=False)

        user.save()
        messages.success(request, 'User created successfully!')
        return redirect('user_list')

    return render(request, 'admin_add_user.html')

@login_required
def user_list_view(request):
    # Ensure only admins can access this view
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to view users.')
        return redirect('home')

    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_welcome_view(request):
    return render(request, 'admin_welcome.html')
