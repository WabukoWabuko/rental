# rental/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Property, Booking, RentPayment, Complaint, Chat, HouseAvailability
from .forms import PropertyForm, BookingForm, RentPaymentForm, ComplaintForm, ChatForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    """
    Display the home page with a list of available properties.
    """
    properties = Property.objects.filter(availability=True)
    return render(request, 'home.html', {'properties': properties})

@login_required
def property_detail(request, property_id):
    """
    Display details of a specific property, including availability, description, and location.
    """
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'property_detail.html', {'property': property})

@login_required
def book_property(request, property_id):
    """
    Handle property booking by the tenant.
    """
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tenant = request.user
            booking.property = property
            booking.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'book_property.html', {'form': form, 'property': property})

@login_required
def pay_rent(request, property_id):
    """
    Process rent payment for a specific property.
    """
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = RentPaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.tenant = request.user
            payment.property = property
            payment.save()
            return redirect('payment_confirmation')
    else:
        form = RentPaymentForm()
    return render(request, 'pay_rent.html', {'form': form, 'property': property})

@login_required
def submit_complaint(request, property_id):
    """
    Allow tenants to submit complaints or requests for a property.
    """
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.tenant = request.user
            complaint.property = property
            complaint.save()
            return redirect('complaint_confirmation')
    else:
        form = ComplaintForm()
    return render(request, 'submit_complaint.html', {'form': form, 'property': property})

@login_required
def chat(request, property_id):
    """
    Chat section for tenants associated with a specific property.
    """
    property = get_object_or_404(Property, id=property_id)
    chats = Chat.objects.filter(property=property)
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = request.user
            chat.property = property
            chat.save()
            return redirect('chat', property_id=property.id)
    else:
        form = ChatForm()
    return render(request, 'chat.html', {'form': form, 'chats': chats, 'property': property})


def logout_view(request):
    # Log out the user
    logout(request)
    # Redirect to the home page or login page after logging out
    return redirect('home')  # Replace 'home' with the name of your desired redirect URL


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')  # The login page template

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.email.POST['email']
        password_confirm = request.POST['password_confirm']
        
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully. You can now log in.')
                return redirect('login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'signup.html')  # The signup page template

def properties_list(request):
    properties = Property.objects.all()
    return render(request, 'properties_list.html', {'properties': properties})

def contact(request):
    return render(request, 'contact.html')