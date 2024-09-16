from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.http import HttpResponseForbidden

def home(request):
    return render(request, 'index.html')




def add_reservation(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer')
        customer_mobile = request.POST.get('customerM')
        customer_email = request.POST.get('customerE')
        
        if not customer_name or not customer_mobile or not customer_email:
            messages.error(request, 'All fields are required.')
            return redirect('add_reservation')

        customer = Customer(Cname=customer_name, Cnumber=customer_mobile, Cemail=customer_email)
        customer.save()
        
        messages.success(request, 'Reservation added successfully.')
        return redirect('view_reservations')


    return render(request, 'AddReservation.html')

def add_hotel(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add hotels.')
        return redirect('home')
    
    if request.method == 'POST':
        hotel_name = request.POST.get('hname')
        hotel_price = request.POST.get('hprice')
        hotel_location = request.POST.get('hlocation')
        
        if not hotel_name or not hotel_price or not hotel_location:
            messages.error(request, 'All fields are required.')
            return redirect('add_hotel')
        
        # Create and save the hotel instance
        hotel = Hotel(name=hotel_name, price=hotel_price, location=hotel_location)
        hotel.save()
        
        messages.success(request, 'Hotel added successfully.')
        return redirect('available')
    
    return render(request, 'AddHotel.html')

def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    
    if request.method == 'POST':
        customer.Cname = request.POST.get('Cname')
        customer.Cnumber = request.POST.get('Cnumber')
        customer.Cemail = request.POST.get('Cemail')
        customer.save()
        messages.success(request, 'Customer updated successfully!')
        return redirect('view_reservations')  # Redirect to the customer list view

    return render(request, 'edit_customer.html', {'customer': customer})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to delete this customer.')
    customer.delete()
    messages.success(request, 'Customer deleted successfully!')
    return redirect('view_reservations')



def edit_hotel(request, id):
    hotel = get_object_or_404(Hotel, id=id)

    if request.method == 'POST':
        hotel.name = request.POST.get('hname')
        hotel.price = request.POST.get('hprice')
        hotel.location = request.POST.get('hlocation')
        hotel.save()
        messages.success(request, 'Hotel updated successfully!')
        return redirect('available')  

    return render(request, 'edit_hotel.html', {'hotel': hotel})

def delete_hotel(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    hotel.delete()
    messages.success(request, 'Customer deleted successfully!')
    return redirect('available')

def Available(request):
    hotels = Hotel.objects.all() 
    return render(request, 'AvailableHotels.html', {'hotels': hotels})

def view_reservations(request):
    customers = Customer.objects.all() 
    return render(request, 'ViewReservation.html', {'customers' : customers})

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
