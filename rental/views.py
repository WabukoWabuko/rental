# rental/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Property, Booking, RentPayment, Complaint, Chat, HouseAvailability
from .forms import PropertyForm, BookingForm, RentPaymentForm, ComplaintForm, ChatForm

def home(request):
    """
    Display the home page with a list of available properties.
    """
    properties = Property.objects.filter(availability=True)
    return render(request, 'rental/home.html', {'properties': properties})

@login_required
def property_detail(request, property_id):
    """
    Display details of a specific property, including availability, description, and location.
    """
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'rental/property_detail.html', {'property': property})

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
    return render(request, 'rental/book_property.html', {'form': form, 'property': property})

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
    return render(request, 'rental/pay_rent.html', {'form': form, 'property': property})

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
    return render(request, 'rental/submit_complaint.html', {'form': form, 'property': property})

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
    return render(request, 'rental/chat.html', {'form': form, 'chats': chats, 'property': property})
